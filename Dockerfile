# syntax=docker/dockerfile:experimental

#### Base stage
FROM python:3.9.4-slim as python_base

LABEL authors="me.raddadi@gmail.com"

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    POETRY_PATH=/opt/poetry \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    VENV_PATH=/opt/venv \
    POETRY_VERSION=1.1.6

ENV PATH="$POETRY_PATH/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update -qq && apt install -qq -yy procps curl


#### Build stage
FROM python_base as build_image

RUN mkdir /app && useradd library-user && chown -hR library-user:library-user /app/ && \
    apt-get update -qq && apt install -qq -yy ca-certificates build-essential  && \
    curl -ssL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python \
    && mv /root/.poetry $POETRY_PATH \
    && poetry --version \
    && python -m venv $VENV_PATH \
    && poetry config virtualenvs.create false \
    # cleanup
    && rm -rf /var/lib/apt/lists/* \
    && chown -hR library-user:library-user /app


COPY poetry.lock pyproject.toml /app/
COPY src/ /app/src

WORKDIR /app

RUN poetry install --no-dev --no-interaction --no-ansi -vvv


#### Dev stage
FROM build_image as dev

RUN poetry install

# Copy code in
COPY --chown=library-user:library-user . /app

USER library-user

CMD ["python", "/app/src/upciti/main.py"]


#### Prod stage
FROM python_base as prod

WORKDIR /app

RUN useradd library-user
COPY --chown=library-user:library-user --from=build_image /app /app
COPY --from=build_image $VENV_PATH $VENV_PATH 

# Copy code in
COPY --chown=library-user:library-user . /app

USER library-user

CMD ["python", "/app/src/upciti/main.py"]
