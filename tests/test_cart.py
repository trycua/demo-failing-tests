import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from cart import apply_discount, total  # noqa: E402


class CartTest(unittest.TestCase):
    def test_ten_percent_off(self):
        self.assertEqual(apply_discount(2000, 10), 1800)

    def test_cart_total_with_discount(self):
        self.assertEqual(total([1000, 2000], 50), 1500)


if __name__ == "__main__":
    unittest.main()
