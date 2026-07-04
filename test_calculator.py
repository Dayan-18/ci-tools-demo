"""Test suite executed by every CI tool in this repo (same tests, 3 pipelines)."""
import pytest

from calculator import apply_discount, subtotal, total_with_tax


def test_subtotal_sums_price_times_quantity():
    assert subtotal([(10.0, 2), (5.0, 3)]) == 35.0


def test_subtotal_empty_cart_is_zero():
    assert subtotal([]) == 0


def test_subtotal_rejects_negative_values():
    with pytest.raises(ValueError):
        subtotal([(-1.0, 2)])


@pytest.mark.parametrize("amount,percent,expected", [
    (100.0, 0, 100.0),
    (100.0, 10, 90.0),
    (100.0, 100, 0.0),
    (59.99, 25, 44.99),
])
def test_apply_discount(amount, percent, expected):
    assert apply_discount(amount, percent) == expected


def test_apply_discount_rejects_invalid_percent():
    with pytest.raises(ValueError):
        apply_discount(100.0, 150)


def test_total_with_tax_default_18_percent():
    assert total_with_tax(100.0) == 118.0


def test_total_with_tax_custom_rate():
    assert total_with_tax(200.0, tax_rate=0.10) == 220.0
