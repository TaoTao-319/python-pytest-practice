from decimal import Decimal

import pytest

from qa_utils.cart import calculate_cart_total


def test_missing_unit_price_is_rejected(sample_cart):

    del sample_cart[0]["unit_price"]
    with pytest.raises(ValueError, match="第 1 个商品的 unit_price 无效"):
        calculate_cart_total(sample_cart)


def test_missing_quantity_is_rejected(sample_cart):
    del sample_cart[0]["quantity"]
    with pytest.raises(ValueError, match="第 1 个商品的 quantity"):
        calculate_cart_total(sample_cart)


def test_boolean_quantity_is_rejected(sample_cart):
    sample_cart[0]["quantity"] = True
    with pytest.raises(ValueError, match="quantity"):
        calculate_cart_total(sample_cart)


def test_nan_price_is_rejected(sample_cart):
    sample_cart[0]["unit_price"] = "NaN"
    with pytest.raises(ValueError, match="unit_price"):
        calculate_cart_total(sample_cart)


def test_zero_price_is_allowed(sample_cart):
    sample_cart[0]["unit_price"] = "0.00"
    assert calculate_cart_total(sample_cart) == Decimal("10.00")
