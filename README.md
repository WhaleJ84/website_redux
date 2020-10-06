# Personal Website

This document outlines the instructions to get the website deployed into a Docker container.

```
docker build --rm --no-cache -t personal_website .
docker run -p 5001:5000 personal_website
```