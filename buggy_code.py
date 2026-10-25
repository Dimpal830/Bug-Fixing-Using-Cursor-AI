# BEFORE: a small shopping cart module that contains 5 bugs.
# Run it to see the wrong results.


def add_item(item, cart=[]):  # Bug 1: mutable default argument
    cart.append(item)
    return cart


def calculate_total(prices):
    total = 0
    for i in range(1, len(prices)):  # Bug 2: starts at 1, skips the first price
        total += prices[i]
    return total


def apply_discount(total, percent):
    return total - total * percent  # Bug 3: 10 (%) is treated as 10x, not 10%


def average_price(prices):
    return sum(prices) / len(prices)  # Bug 4: crashes on an empty list


def remove_expensive(prices, limit):
    for p in prices:  # Bug 5: removes items from the list while looping over it
        if p > limit:
            prices.remove(p)
    return prices


if __name__ == "__main__":
    print("Bug 1:", add_item("pen"), add_item("book"), "(expected ['pen'] and ['book'])")
    print("Bug 2:", calculate_total([100, 200, 300]), "(expected 600)")
    print("Bug 3:", apply_discount(600, 10), "(expected 540.0)")
    try:
        print("Bug 4:", average_price([]))
    except ZeroDivisionError as error:
        print("Bug 4: crashed with ->", error)
    print("Bug 5:", remove_expensive([100, 500, 600, 200], 300), "(expected [100, 200])")
