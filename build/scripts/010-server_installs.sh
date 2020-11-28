#!/bin/sh

# ensure apt is up to date
apt update
apt upgrade -y

# install necessary packages
sudo apt install -y python3-pip python3-dev python3-setuptools python3-venv build-essential libssl-dev libffi-dev git

# install snapd
apt install -y snapd

# ensure snapd is up to date
snap install core
snap refresh core

# install certbot
snap install --classic certbot

# prepare certbot command
ln -s /snap/bin/certbot /usr/bin/certbot

# install nginx
apt install -y nginx
