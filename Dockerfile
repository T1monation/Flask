FROM python:3.10-slim

ARG BUILD_DEPS="curl"
RUN apt-get update && apt-get install -y $BUILD_DEPS


# Установка poetry
# RUN pip install poetry
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

# ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000
# EXPOSE 5432

# RUN poetry run flask db upgrade
# RUN flask db upgrade

# RUN ./start_app

# ENV DATABASE_URL=postgresql://flask:123456@192.168.1.77/blog

CMD ./start_app