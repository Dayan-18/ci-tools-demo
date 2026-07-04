"""Tiny module under test: a shopping cart price calculator."""


def subtotal(items):
    """items: list of (price, quantity) tuples."""
    if any(p < 0 or q < 0 for p, q in items):
        raise ValueError("price and quantity must be non-negative")
    return sum(p * q for p, q in items)


def apply_discount(amount, percent):
    if not 0 <= percent <= 100:
        raise ValueError("discount must be between 0 and 100")
    return round(amount * (1 - percent / 100), 2)


def total_with_tax(amount, tax_rate=0.18):
    return round(amount * (1 + tax_rate), 2)
