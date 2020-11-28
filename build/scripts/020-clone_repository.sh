#!/bin/sh

# change to www directory
cd /var/www/ || return

# clone down the repository and enter it
git clone https://github.com/WhaleJ84/website_redux.git
cd website_redux || return

# create python venv and activate it
python3 -m venv personal_website-env
source personal_website-env/bin/activate

# update and install pip dependencies
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
