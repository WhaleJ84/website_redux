# Personal Website

This document outlines the instructions to get the website deployed into a Docker container.

```
docker build --rm --no-cache -t personal_website .
docker run -p 5001:5000 personal_website
```

## Backing up the database

```
docker exec personal_website_database_1 /usr/bin/pg_dump -U james -d jameswhale > jameswhale.sql
docker cp personal_website_database_1:/jameswhale.sql ./jameswhale-$(date +"%C%m%d%H%M%S").sql
```