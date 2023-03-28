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

EXPOSE 5000

# ENV DATABASE_URL=postgresql://flask:123456@192.168.1.77/blog

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
