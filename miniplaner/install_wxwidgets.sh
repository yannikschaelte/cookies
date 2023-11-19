set -eux

# TODO set to appropriate number of cores
n_cores=16
wxv="3.0.5"

cd miniplaner
cwd=$(pwd)

# needs <= 3.0.5
# dependencies:
# - sudo apt install libgtk-3-dev

wget https://github.com/wxWidgets/wxWidgets/releases/download/v${wxv}/wxWidgets-${wxv}.tar.bz2
tar -xvjf wxWidgets-${wxv}.tar.bz2

# compile wxwidgets
cd wxWidgets-${wxv}
mkdir ybuild && cd ybuild
../configure --disable-shared --prefix=${cwd}/wxwidgets
make -j${n_cores}
make install
make clean
cd ..  # to wxwidgets
cd ..  # to base
rm -rf wxWidgets-${wxv}.tar.bz2
