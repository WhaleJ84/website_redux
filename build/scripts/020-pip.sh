#!/bin/bash
# NOTE: this is the only script with the bash interpreter
# This is because the `source` command is not defined in POSIX shell
# If anybody knows how I would do the same in shell, please let me know!

# ensure in correct working directory
cd /var/www/website_redux/ || return

# create python venv and activate it
python3 -m venv personal_website-env
source personal_website-env/bin/activate

# update and install pip dependencies
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
