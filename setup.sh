#!/bin/sh

# exit if variables or commands error
set -eux

for script in build/scripts/*; do
  "./$script"
done
