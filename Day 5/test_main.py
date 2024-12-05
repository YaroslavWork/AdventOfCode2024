import unittest
from main import check_if_order_is_right

class TestGetDistance(unittest.TestCase):
    def test_first_sample(self):
        pages = [
            [47, 53],
            [97, 13],
            [97, 61],
            [97, 47],
            [75, 29],
            [61, 13],
            [75, 53],
            [29, 13],
            [97, 29],
            [53, 29],
            [61, 53],
            [97, 53],
            [61, 29],
            [47, 13],
            [75, 47],
            [97, 75],
            [47, 61],
            [75, 61],
            [47, 29],
            [75, 13],
            [53, 13]
        ]
        self.assertEqual(check_if_order_is_right(pages, [75, 47, 61, 53, 29]), True)
        self.assertEqual(check_if_order_is_right(pages, [97, 61, 53, 29, 13]), True)
        self.assertEqual(check_if_order_is_right(pages, [75, 29, 13]), True)
        self.assertEqual(check_if_order_is_right(pages, [75, 97, 47, 61, 53]), False)
        self.assertEqual(check_if_order_is_right(pages, [61, 13, 29]), False)
        self.assertEqual(check_if_order_is_right(pages, [97, 13, 75, 29, 47]), False)


if __name__ == "__main__":
    unittest.main()