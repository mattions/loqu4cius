#!/usr/bin/env bash

#dev_appserver.py . -d --use_sqlite --datastore_path=tmp/data

dev_appserver.py . --mysql_user=root -d --use_sqlite --datastore_path=tmp/data
