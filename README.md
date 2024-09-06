# test

## Install pipenv
    pip install --user pipenv
More info about [pipenv](https://pipenv.pypa.io/en/latest/)

## Setup for development
Setup for install requirements and configure .env

    pipenv run setup

## Run images(after setup)
Run local docker compose

    pipenv run server

## Run tests(after setup)
Run tests. First it run postgres and redis containers, after that pytest.

    pipenv run db
    pipenv run test


## Run prod server
Run prod docker compose

    pipenv run prod-server

