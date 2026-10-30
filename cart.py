"""A tiny shopping cart. Prices are whole cents."""


def apply_discount(price_cents, percent):
    """The price after taking `percent` percent off."""
    return price_cents * percent // 100


def total(prices_cents, percent=0):
    """The cart total after the discount."""
    return sum(apply_discount(p, percent) for p in prices_cents)
