FROM python:3.10.4-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1
ENV APP_HOME=/app

# install initial dependencies
RUN apt-get update && \
    pip install --no-cache --upgrade pip pipenv

WORKDIR ${APP_HOME}

# install dependencies
COPY Pipfile.lock ${APP_HOME}/
RUN pipenv requirements --dev > ${APP_HOME}/requirements.txt && \
    pip install -r ${APP_HOME}/requirements.txt

# project source is included via volume
# and located at /app/src/
