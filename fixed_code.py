"""Shopping cart helpers.

AFTER: all 5 bugs from buggy_code.py are fixed.
"""


def add_item(item, cart=None):
    """Add an item to a cart. A new list is created if no cart is given."""
    if cart is None:  # Fix 1: never use a mutable default argument
        cart = []
    cart.append(item)
    return cart


def calculate_total(prices):
    """Return the sum of all prices."""
    return sum(prices)  # Fix 2: include every price


def apply_discount(total, percent):
    """Return the total after a percentage discount (0 to 100)."""
    if not 0 <= percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")
    return total * (1 - percent / 100)  # Fix 3: convert percent properly


def average_price(prices):
    """Return the average price, or 0 for an empty list."""
    if not prices:  # Fix 4: handle the empty list
        return 0
    return sum(prices) / len(prices)


def remove_expensive(prices, limit):
    """Return a new list with only the prices at or below the limit."""
    return [p for p in prices if p <= limit]  # Fix 5: build a new list instead


if __name__ == "__main__":
    print("Fix 1:", add_item("pen"), add_item("book"))
    print("Fix 2:", calculate_total([100, 200, 300]))
    print("Fix 3:", apply_discount(600, 10))
    print("Fix 4:", average_price([]))
    print("Fix 5:", remove_expensive([100, 500, 600, 200], 300))
