#!/bin/bash

docker-compose exec db bash -c 'mysqldump -h 127.0.0.1 --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD" > /var/lib/mysql/backup.sql'
