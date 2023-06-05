"""
Approve vacation at the University of Bonn
==========================================

A small script to automatize the filling out of vacation request
standard form at the University of Bonn.

Call:
>>> python approve_vacation_uni_bonn.py --in=request.pdf

Requirements:
>>> pip install pypdf reportlab click PIL

Customize to your needs.
"""

import pypdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PIL import Image
from datetime import datetime
import click


def approve_request(
    input_pdf,
    output_pdf,
    name,
    date,
    signature,
):
    if date is None:
        date = datetime.now().strftime("%d.%m.%Y")
    if output_pdf is None:
        initials = "".join([w[0].lower() for w in name.split()])
        output_pdf = f"{input_pdf[:-4]}_{initials}.pdf"

    # Open the input PDF file
    with open(input_pdf, "rb") as file:
        pdf_reader = pypdf.PdfReader(file)
        page = pdf_reader.pages[0]

        # Create a new PDF file
        c = canvas.Canvas(output_pdf, pagesize=A4)
        c.setFont("Helvetica", 12)

        # Draw approval
        c.drawString(59.5, 185, "x")

        # Draw date
        c.drawString(95, 71, date)

        # Draw name
        c.drawString(330, 60, name)

        # Draw signature
        sgn = Image.open(signature)
        sgn_width = 90
        sgn_height = sgn_width * sgn.size[1] / sgn.size[0]
        c.drawImage(signature, 330, 70, width=sgn_width, height=sgn_height)

        # Add the original PDF content
        c.showPage()
        c.save()

        # Merge the original PDF with the new page
        output = pypdf.PdfWriter()
        with open(output_pdf, "rb") as new_file:
            new_pdf = pypdf.PdfReader(new_file)
            page.merge_page(new_pdf.pages[0])
            output.add_page(page)

        # Write the merged PDF to the output file
        with open(output_pdf, "wb") as merged_file:
            output.write(merged_file)


# Usage example
# input_pdf = 'request_vacation.pdf'
# output_pdf = None
# name = "Yannik Schaelte"
# date = None
# signature = 'signature.png'

# approve_request(
#    input_pdf,
#    output_pdf,
#    name,
#    date,
#    signature,
# )


@click.command()
@click.option("-i", "--in", "in_", type=str, help="Input PDF file", required=True)
@click.option("-o", "--out", type=str, help="Output PDF file", default=None)
@click.option("-n", "--name", type=str, help="Signer's name", default="Yannik Schaelte")
@click.option("-d", "--date", type=str, help="Date", default=None)
@click.option(
    "-s", "--signature", type=str, help="Signature image file", default="signature.png"
)
def main(in_, out, name, date, signature):
    approve_request(in_, out, name, date, signature)


if __name__ == "__main__":
    main()
