from decimal import Decimal

from qa_utils import calculate_cart_total


def test_wrong_expected_total():
    items = [
        {"unit_price": "3.25", "quantity": 2},
        {"unit_price": "10.00", "quantity": 1},
    ]
    actual = calculate_cart_total(items)
    assert actual == Decimal("16.00")
