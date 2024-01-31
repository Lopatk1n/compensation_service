FROM python:3.10
ENV PYTHONUNBUFFERED 1
ENV CGO_ENABLED 1

WORKDIR /src
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock .

RUN poetry install --no-interaction --no-ansi --no-root

