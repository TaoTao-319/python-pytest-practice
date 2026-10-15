import pytest


@pytest.fixture(scope="function")
def sample_cart():
    return [
        {"unit_price": "3.25", "quantity": 2},
        {"unit_price": "10.00", "quantity": 1},
    ]
