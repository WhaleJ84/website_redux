# Personal Website

[![Build Status](https://travis-ci.com/WhaleJ84/website_redux.svg?token=bQrzTEEcDB4TnMh7bfsH&branch=main)](https://travis-ci.com/WhaleJ84/website_redux)
[![codecov](https://codecov.io/gh/WhaleJ84/website_redux/branch/main/graph/badge.svg?token=X7ISO9NP60)](https://codecov.io/gh/WhaleJ84/website_redux)

This document outlines the instructions to get the website deployed into a Docker container.

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
