from upciti.dummy import dummy_function


def test_dummy_function():
    assert dummy_function(1, 2) == 3
