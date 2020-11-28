#!/bin/sh

# create nginx file if it doesn't exist
[ ! -f '/etc/nginx/sites-available/jameswhale' ] && cat > /etc/nginx/sites-available/jameswhale << EOF
server {
    listen 80;
    listen [::]:80;

    server_name james-whale.com www.james-whale.com;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/var/www/website_redux/jameswhale.sock;
    }
}
EOF

# make site available
[ ! -e '/etc/nginx/sites-enabled/jameswhale' ] && ln -s /etc/nginx/sites-available/jameswhale /etc/nginx/sites-enabled

# check for errors
nginx -t && systemctl restart nginx || return
