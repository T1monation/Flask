FROM python:3.7-slim

ARG BUILD_DEPS="curl"
RUN apt-get update && apt-get install -y $BUILD_DEPS


RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.3.2 POETRY_HOME=/root/poetry python3 -
ENV PATH="${PATH}:/root/poetry/bin"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

RUN poetry install --no-dev

ENV DATABASE_URL: postgres://db_for_my_test_app_user:kNa63nTroqfwpdtwRnsdtfOLhlfZPjLM@dpg-cgg1emm4daddcg1s40t0-a.frankfurt-postgres.render.com/db_for_my_test_app

RUN chmod +x ./start_app


EXPOSE 8000

RUN ./start_app

