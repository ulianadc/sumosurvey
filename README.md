# SumoSurvey

To get this up and running, you'll need Docker and [Docker Compose](https://docs.docker.com/compose/).

From the repo root, run `docker-compose build` to fetch the base images and build the Python/Django env, and `docker-compose up -d` to get things going. It may be necessary to `docker-compose restart server` if the server does not initially respond on `localhost:8000`, which I imagine is due to the database service booting up more slowly.

I have some simple survey questions already populated in the database, which is dumped to the repo at `db/mysql/backup.sql`. Once the mysql container is up and running, import via `./db_import.sh` (no args).

The lone superuser account is `admin` (password `sumopants`), and can be used to login to either `localhost:8000/admin` or `localhost:8000/surveys/manage`.

Lots more I'd like to do, but ran out of time. Django is interesting and quite a bit more sophisticated than I anticipated. I'm curious about how it scales.

![Screenshot](https://raw.github.com/ulianadc/sumosurvey/master/screenshot.png)
