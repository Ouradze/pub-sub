from invoke import task  # type: ignore


# TODO(ouradze): fix type hinting
# Use: https://github.com/pyinvoke/invoke/issues/357
@task
def black(c):
    """Run check on files with black."""
    print("Running black check")
    c.run("black --diff --check .", pty=True)


@task
def flake8(c):
    """Run check on files with flake8."""
    print("Running flake8 check")
    c.run("flake8 --show-source .", pty=True)


@task
def isort(c):
    """Run check on files with isort."""
    print("Running isort check")
    c.run("isort . -cq -df", pty=True)


@task
def bandit(c):
    """Run check on files with bandit."""
    print("Running bandit check")
    # NOTE: use .bandit file when
    # https://github.com/PyCQA/bandit/issues/657 is resolved
    excluded_files = "venv,test_*.py,tests_*.py,tests,test"
    c.run(
        f"bandit --exclude '{excluded_files}' --quiet -n 2 --format screen -r .",
        pty=True,
    )


@task
def mypy(c):
    """Run check on files with mypy."""
    print("Running mypy check")
    c.run("mypy . --exclude tests", pty=True)


@task(black, flake8, isort, bandit, mypy)
def quality(c):
    """Run all quality checks on files."""
    print("Quality checks successful")


@task(
    help={
        "local": "Use this option for terminal coverage and no xml output. Not activated by default."
    }
)
def coverage(c, local=False):
    """Run pytest with coverage."""
    print("Running unit tests and coverage report")

    coverage_option = "--cov-report=xml" if not local else ""
    c.run(
        f"pytest --cov=src {coverage_option} --no-cov-on-fail --cov-branch --color=yes",
        pty=True,
    )
