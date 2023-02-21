#!/bin/sh

# begin modify
BASE=$PWD
ENV="env"
# end modify

CONDA_DIR=$BASE/miniconda3

# load anaconda
eval "$($CONDA_DIR/bin/conda shell.bash hook)"

# activate conda environment
conda activate $ENV
