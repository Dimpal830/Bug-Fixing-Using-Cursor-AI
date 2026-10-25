# Bug Fixing with Cursor AI

A debugging exercise. `buggy_code.py` is a small shopping cart module with 5 bugs. `fixed_code.py` is the corrected version, and `test_fixed.py` proves every fix works.

## The bugs and the fixes

| # | Bug in `buggy_code.py` | What went wrong | Fix in `fixed_code.py` |
|---|---|---|---|
| 1 | `cart=[]` as a default argument | The same list is shared between calls, so items from different carts mix | Use `cart=None` and create a new list inside the function |
| 2 | `range(1, len(prices))` | Starts at 1, so the first price is skipped (total 500 instead of 600) | Use `sum(prices)` |
| 3 | `total - total * percent` | A 10% discount is treated as 10x, giving a negative total | Use `total * (1 - percent / 100)` and validate the range |
| 4 | `sum(prices) / len(prices)` | Crashes with `ZeroDivisionError` on an empty list | Return 0 when the list is empty |
| 5 | `prices.remove(p)` inside `for p in prices` | Removing while looping skips items | Build a new list with a list comprehension |

## How I used Cursor AI

(Write this part in your own words: how you found the bugs, which prompts you gave Cursor, what it suggested, and what you checked yourself.)

## How to run

```bash
python buggy_code.py     # shows the wrong results
python fixed_code.py     # shows the correct results
python test_fixed.py     # runs the tests
```

## Technologies
Python, debugging, Cursor AI, unit testing basics
