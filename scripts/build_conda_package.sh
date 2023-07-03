#!/bin/bash
set -e
# Get the directory of this script
SCRIPT_DIR="$(dirname "$0")"

# Change to the script's directory
cd "$SCRIPT_DIR"/..

# Build the conda package
conda build --croot ./build_conda --output-folder ./build_conda ./conda.recipe
