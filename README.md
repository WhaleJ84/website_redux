# Personal Website

![CI](https://github.com/WhaleJ84/website_redux/workflows/CI/badge.svg)
[![Build Status](https://travis-ci.com/WhaleJ84/website_redux.svg?token=bQrzTEEcDB4TnMh7bfsH&branch=main)](https://travis-ci.com/WhaleJ84/website_redux)
[![codecov](https://codecov.io/gh/WhaleJ84/website_redux/branch/main/graph/badge.svg?token=X7ISO9NP60)](https://codecov.io/gh/WhaleJ84/website_redux)

This is the repository for the rewrite of my original website designed as a static HTML site.
The rewrite uses the Python [Flask microframework](https://flask.palletsprojects.com/en/1.1.x/) and integrates with a [PostgreSQL container](https://hub.docker.com/_/postgres) for the blog entries.

Originally both the website and the database were in separate containers, but I faced issues trying to get [Certbot](https://certbot.eff.org/) SSL certificates working with the [website container](https://hub.docker.com/r/tiangolo/meinheld-gunicorn-flask).
I eventually plan to move it back to having everything containerised but I prioritise having HTTPS over that.

Along with the rewrite, I am using this opportunity to learn more about CI/CD and delve more into DevOps.
I currently have a CI workflow going with [Travis CI](https://travis-ci.com/) and will (eventually) get around to implementing CD.

## Initial Setup

Provided a server is available and a DNS entry for the domain correctly set up, following the commands below should set up the web server from scratch.

```
apt update && apt install -y git
cd /var/www
git clone https://github.com/WhaleJ84/website_redux.git
cd  website_redux
./setup.sh
```

## Managing the app

As the installation script sets up a systemd service, both `nginx` and `uwsgi` can be handled as such:

```
# nginx
systemctl {stop,start,restart} nginx

# uwsgi
systemctl {stop,start} jameswhale
```

If any changes have been made to the Flask application itself, uWSGI will have to be stopped and started again to reflect the changes.

## Older instructions for website container

```
docker build --rm --no-cache -t personal_website .
docker-compose up -d
```

## Database

This section outlines how to backup and restore the database between deployments.

### Backup

```
docker exec database /usr/bin/pg_dump -U james -d jameswhale > build/database/jameswhale.sql
```

### Restore

```
docker cp database_dumps/jameswhale.sql personal_website_database_1:/jameswhale.sql
docker exec personal_website_database_1 /usr/bin/psql -U james -d jameswhale -f jameswhale.sql
```

## Sensitive docs to be removed

The 'sensitive' docs mentioned here have purposely had bad creds chosen for them as they will be changed and serve no immediate risk.
I am noting them here so I can migrate the instances to more secure methods.

### .travis.yml postgres credentials (purposely bad)

Seemingly the only way to encrypt values for travis is to use a CLI program.
Screw `travis login`.
Trying to log into said program seems impossible - therefore this credential remains in cleartext.
Travis builds a brand new postgres instance and imports the table anyway.
