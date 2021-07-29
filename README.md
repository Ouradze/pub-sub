# Pub-Sub

[![codecov](https://codecov.io/gh/Ouradze/pub-sub/branch/master/graph/badge.svg?token=4ZCPVN78XH)](https://codecov.io/gh/Ouradze/pub-sub)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![CI](https://github.com/Ouradze/pub-sub/actions/workflows/ci.yml/badge.svg)

Project pub-sub test with upciti

## Requirements

### Lefthook

Lefthook is mandatory, that' a tool which run predefined scripts on git hooks. We're using it to ensure that what you push respects our quality rules.

First of all, you'll have to install it globally

```bash
npm install @arkweid/lefthook --global
```

Then, you'll have to run it locally. This step will tell Lefthook to install custom hooks in your local .git directory

```bash
npx @arkweid/lefthook install pre-push
```

Voilà, Lefthook is working and will run scripts defined in lefthook.yml file on push event.

Want to run it manually? No problem you can do that by running

```bash
npx @arkweid/lefthook run pre-push
```

### Docker

You must have [docker](https://docs.docker.com/engine/install/) and [docker compose](https://docs.docker.com/compose/install/) installed on your computer for the containers to work.
Please refer to their documentation for installation.

### Pyenv

I suggest using [pyenv](https://github.com/pyenv/pyenv) to manage your python versions.

### Poetry

This project uses [poetry](https://python-poetry.org/docs/) for dependency management you will need it to install the project and its dependencies.

## Setup

1. Clone the project
2. Activate python 3.9.4 with `pyenv local 3.9.4`
3. Install dependencies with `poetry install`
4. Activate the venv with `poetry shell`
5. Use the project with either `python src/upciti/main.py` or `invoke run` for the container version

If you need to find the available commands for you, you can use: `invoke --list`. For specific help, please use: `invoke cmd --help`.

## To go further

1. Improve the first implementation of the pub sub.
2. Use redis with compose to have multiple workers as well as processes to exchange data between themselves.
3. Publish a python package to install the wheel in the docker image rather than what is currently used.
4. Remove factory-boy from the production code to fix the production image. This would mean another service or image
would send the information for instance via http or redis.
5. Use click or similar to create a real cli.
