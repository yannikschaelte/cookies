set -eux

cd miniplaner
cwd=$(pwd)

# get wxwidgets
export PATH=${cwd}/wxwidgets/bin:${cwd}/wxwidgets/include:${cwd}/wxwidgets/lib:$PATH

# get meson
eval "$(miniconda3/bin/conda shell.bash hook)"
conda activate miniplaner

cd miniplaner
meson setup build && cd build
meson compile

cd ..  # to miniplaner
cd ..  # to base
