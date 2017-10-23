#!/bin/bash

dc exec db bash -c 'mysql -h 127.0.0.1 -uroot -p"$MYSQL_ROOT_PASSWORD" < /var/lib/mysql/backup.sql'
