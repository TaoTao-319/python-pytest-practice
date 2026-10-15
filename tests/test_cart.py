from decimal import Decimal

import pytest

from qa_utils.cart import calculate_cart_total


@pytest.mark.parametrize(
    "quantity, expected",
    [
        pytest.param(0, Decimal("10.00"), id="zero_quantity"),
        pytest.param(1, Decimal("13.25"), id="one_item"),
        pytest.param(3, Decimal("19.75"), id="three_items"),
    ],
)
def test_total_after_changing_quantity(sample_cart, quantity, expected):


    sample_cart[0]["quantity"] = quantity
    assert calculate_cart_total(sample_cart) == expected


def test_empty_cart(sample_cart):
    sample_cart.clear()
    assert calculate_cart_total(sample_cart) == Decimal("0.00")


def test_total_after_adding_item(sample_cart):
    sample_cart.append({"unit_price": "2.00", "quantity": 2})
    assert calculate_cart_total(sample_cart) == Decimal("20.50")


def test_total_after_removing_item(sample_cart):
    sample_cart.pop()
    assert calculate_cart_total(sample_cart) == Decimal("6.50")


def test_negative_quantity_is_rejected(sample_cart):
    sample_cart[0]["quantity"] = -1


    with pytest.raises(ValueError, match="quantity"):
        calculate_cart_total(sample_cart)


def test_negative_price_is_rejected(sample_cart):
    sample_cart[0]["unit_price"] = "-1.00"
    with pytest.raises(ValueError, match="unit_price"):
        calculate_cart_total(sample_cart)


def test_original_cart_total(sample_cart):
    assert calculate_cart_total(sample_cart) == Decimal("16.50")
