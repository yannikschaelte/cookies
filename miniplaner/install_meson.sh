set -eux

cd miniplaner

# install conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
mkdir miniconda3
bash miniconda3.sh -b -u -p miniconda3
rm -rf miniconda3.sh
# add to path
eval "$(miniconda3/bin/conda shell.bash hook)"
which conda
# create environment
conda create -n miniplaner python=3.11 -y
conda activate miniplaner
# install meson
pip install meson ninja
