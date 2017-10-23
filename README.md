# SumoSurvey

To get this up and running, you'll need Docker and [Docker Compose](https://docs.docker.com/compose/).

From the project directory, run `docker-compose build` to fetch the base images and build the Python/Django env, and `docker-compose up -d` to get things going. It may be necessary to `docker-compose restart server` if the server does not response on `localhost:8000`.

I have some simple surveys already populated in the database. Once the mysql container is up and running, import via `./db_import.sh`. The lone superuser account is `admin` (password `sumopants`), and can be used to login to either `localhost:8000/admin` or `http://localhost:8000/surveys/manage`.

Lots more I'd like to do, but ran out of time. Django is interesting and quite a bit more sophisticated than I anticipated. I'm curious about how it scales.
