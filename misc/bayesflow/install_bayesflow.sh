#!/bin/sh

# install miniconda
sh ../miniconda/install_miniconda.sh

# activate environment
. ../miniconda/activate_env.sh

# download bayesflow
git clone git@github.com:stefanradev93/bayesflow.git

cd bayesflow

# checkout develop
git checkout Development

# install bayesflow in editable mode
pip install -e .
