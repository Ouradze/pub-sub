import os

import factory.random
import pytest


os.environ.setdefault("PYTHONBREAKPOINT", "ipdb.set_trace")


@pytest.fixture(autouse=True)
def seed_factory_boy() -> None:
    """
    Give the same seed to factory-boy to prevent snapshot tests from failing because
    of changing data.
    """
    factory.random.reseed_random("16159953954273")
