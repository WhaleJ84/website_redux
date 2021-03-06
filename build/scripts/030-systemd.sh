#!/bin/sh

# create systemd service file if it doesn't exist
[ ! -e '/etc/systemd/system/jameswhale.service' ] && cat > /etc/systemd/system/jameswhale.service << EOF
[Unit]
Description=uWSGI instance to serve jameswhale
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/website_redux
Environment="PATH=/var/www/website_redux/venv/bin"
ExecStart=/var/www/website_redux/venv/bin/uwsgi --ini build/website/jameswhale.ini

[Install]
WantedBy=multi-user.target
EOF

# confirm service is enabled and running
systemctl start jameswhale
systemctl enable jameswhale
