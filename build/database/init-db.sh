#!/bin/sh
set -e

psql -U james -d jameswhale -f /tmp/jameswhale.sql
