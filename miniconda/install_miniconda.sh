#!/bin/sh

set -eux

# begin modify
BASE=$PWD
ENV="env"
PYTHON_V="3.10"
# end modify

CONDA_DIR=$BASE/miniconda3

# install conda environment
if [ ! -e $CONDA_DIR ]; then
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
  bash miniconda3.sh -b -p $CONDA_DIR
  rm miniconda3.sh
fi

# create conda environment
eval "$($CONDA_DIR/bin/conda shell.bash hook)"
conda create -y -n $ENV python=$PYTHON_V


