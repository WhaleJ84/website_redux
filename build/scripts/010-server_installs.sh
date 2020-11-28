#!/bin/sh

# ensure apt is up to date
apt update
apt upgrade -y

# install necessary system packages
apt apt install -y build-essential libssl-dev libffi-dev snapd nginx

# install necessary python packages
apt install -y python3-pip python3-dev python3-setuptools python3-venv python3-certbot-nginx

# ensure snapd is up to date
snap install core
snap refresh core

# install certbot
snap install --classic certbot
