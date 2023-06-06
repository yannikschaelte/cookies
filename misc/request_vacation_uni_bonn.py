"""
Request vacation at the University of Bonn
==========================================

A small script to automatize the filling out of vacation request
standard forms at the University of Bonn.

Call:
>>> python request_vacation_uni_bonn.py --date_from=01.08.2023 --date_to=30.09.2023

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
import os


def date2str(date):
    return datetime.strptime(date, "%Y%m%d").strftime("%d.%m.%Y")


@click.command()
@click.option(
    "-i",
    "--in",
    "input_pdf",
    type=str,
    help="Input PDF file",
    default="request_vacation.pdf",
)
@click.option(
    "-o", "--out", "output_pdf", type=str, help="Output PDF file", default=None
)
@click.option(
    "-n", "--name", "name", type=str, help="Requester's name", default="Yannik Schaelte"
)
@click.option(
    "-d", "--date", "date", type=str, help="Date in format %Y%m%d", default=None
)
@click.option(
    "-f",
    "--from",
    "date_from",
    type=str,
    help="Date from in format %Y%m%d",
    required=True,
)
@click.option(
    "-t", "--to", "date_to", type=str, help="Date to in format %Y%m%d", required=True
)
@click.option(
    "-s",
    "--signature",
    "signature",
    type=str,
    help="Signature image file",
    default="signature.png",
)
@click.option(
    "-w",
    "--overwrite",
    "overwrite",
    type=bool,
    help="Overwrite output file",
    is_flag=True,
    show_default=True,
    default=False,
)
def request(
    input_pdf,
    output_pdf,
    name,
    date,
    date_from,
    date_to,
    signature,
    overwrite,
):
    # default date is today
    if date is None:
        date = datetime.now().strftime("%Y%m%d")

    # output file name
    if output_pdf is None:
        output_pdf = f"request_vacation_{name.strip()}_{date_from}.pdf"

    # check if output file exists
    if os.path.exists(output_pdf) and not overwrite:
        raise OSError(f"File exists: {output_pdf}")

    # Open the input PDF file
    with open(input_pdf, "rb") as file:
        pdf_reader = pypdf.PdfReader(file)
        page = pdf_reader.pages[0]

        # Create a new PDF file
        c = canvas.Canvas(output_pdf, pagesize=A4)
        c.setFont("Helvetica", 12)

        # Draw name
        c.drawString(70, 777, name)

        # Draw date
        c.drawString(435, 709, date2str(date))

        # Draw request x
        request_y = 564
        c.drawString(158.5, request_y - 1, "x")
        # Draw date from and to
        c.drawString(280, request_y, date2str(date_from))
        c.drawString(380, request_y, date2str(date_to))

        # Draw signature
        sgn = Image.open(signature)
        sgn_width = 90
        sgn_height = sgn_width * sgn.size[1] / sgn.size[0]
        c.drawImage(signature, 70, 257, width=sgn_width, height=sgn_height)

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
# input_pdf = "request_vacation.pdf"
# output_pdf = None
# name = "Yannik Schaelte"
# date = None
# date_from = "09.06.2023"
# date_to = "09.06.2023"
# signature = "signature.png"

# request(
#    input_pdf,
#    output_pdf,
#    name,
#    date,
#    date_from,
#    date_to,
#    signature,
# )

if __name__ == "__main__":
    request()
