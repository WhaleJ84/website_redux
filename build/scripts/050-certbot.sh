#!/bin/sh

# create certbot symlink if it doesn't exist
[ ! -e '/usr/bin/certbot' ] && ln -s /snap/bin/certbot /usr/bin/certbot

# get ssl certificates
certbot --nginx --noninteractive --redirect -d james-whale.com -d www.james-whale.com

# create monthly renew job if it doesn't exist
[ ! -f '/etc/cron.d/jameswhale' ] && cat > /etc/cron.d/jameswhale << EOF
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

1 1 1 * * root certbot renew
EOF
