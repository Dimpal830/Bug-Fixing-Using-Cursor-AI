"""Simple tests for fixed_code.py. Run with: python test_fixed.py"""

from fixed_code import (
    add_item, calculate_total, apply_discount, average_price, remove_expensive,
)


def test_add_item_does_not_share_cart():
    assert add_item("pen") == ["pen"]
    assert add_item("book") == ["book"]


def test_calculate_total_includes_first_price():
    assert calculate_total([100, 200, 300]) == 600


def test_apply_discount_percent():
    assert apply_discount(600, 10) == 540
    assert apply_discount(600, 0) == 600


def test_apply_discount_rejects_bad_percent():
    try:
        apply_discount(600, 150)
    except ValueError:
        return
    raise AssertionError("Expected ValueError")


def test_average_price_empty_list():
    assert average_price([]) == 0
    assert average_price([10, 20]) == 15


def test_remove_expensive():
    assert remove_expensive([100, 500, 600, 200], 300) == [100, 200]


if __name__ == "__main__":
    tests = [v for k, v in list(globals().items()) if k.startswith("test_")]
    for test in tests:
        test()
        print("PASS", test.__name__)
    print(f"\nAll {len(tests)} tests passed.")
