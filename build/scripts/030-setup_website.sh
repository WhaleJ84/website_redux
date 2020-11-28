#!/bin/sh

# copy systemd service file
cp ../website/jameswhale.service /etc/systemd/system/jameswhale.service

# confirm service is enabled and running
systemctl start jameswhale
systemctl enable jameswhale
systemctl status jameswhale
