#!/bin/sh

# copy nginx files to correct location
cp ../website/jameswhale /etc/nginx/sites-available/jameswhale

# make site available
ln -s /etc/nginx/sites-available/jameswhale /etc/nginx/sites-enabled

# check for errors
nginx -t && systemctl restart nginx || return
