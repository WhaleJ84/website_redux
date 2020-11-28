# Personal Website

[![Build Status](https://travis-ci.com/WhaleJ84/website_redux.svg?token=bQrzTEEcDB4TnMh7bfsH&branch=main)](https://travis-ci.com/WhaleJ84/website_redux)
[![codecov](https://codecov.io/gh/WhaleJ84/website_redux/branch/main/graph/badge.svg?token=X7ISO9NP60)](https://codecov.io/gh/WhaleJ84/website_redux)

This is the repository for the rewrite of my original website designed as a static HTML site.
The rewrite uses the Python [Flask microframework](https://flask.palletsprojects.com/en/1.1.x/) and integrates with a [PostgreSQL container](https://hub.docker.com/_/postgres) for the blog entries.

Originally both the website and the database were in separate containers, but I faced issues trying to get [Certbot](https://certbot.eff.org/) SSL certificates working with the [website container](https://hub.docker.com/r/tiangolo/meinheld-gunicorn-flask).
I eventually plan to move it back to having everything containerised but I prioritise having HTTPS over that.

Along with the rewrite, I am using this opportunity to learn more about CI/CD and delve more into DevOps.
I currently have a CI workflow going with [Travis CI](https://travis-ci.com/) and will (eventually) get around to implementing CD.

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

# NOTES

## Sensitive docs to be removed

The 'sensitive' docs mentioned here have purposely had bad creds chosen for them as they will be changed and serve no immediate risk.
I am noting them here so I can migrate the instances to more secure methods.

- .travis.yml > before_script: postgres creds (purposely bad)
- codecov.yml > token (will be obsolete when repo goes public)
- build/docker-compose.yml > database: environment: POSTGRES_PASSWORD (purposely bad)
- personal_website/config.py > SECRET_KEY (easily regenerated)
- personal_website/config.py > SQLALCHEMY_DATABASE_URI's (purposely bad)
