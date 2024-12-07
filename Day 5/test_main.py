import unittest
from main import check_if_order_is_right, change_order_position_to_right_format


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


class TestGetDistance(unittest.TestCase):
    def test_first_sample(self):
        self.assertIsInstance(check_if_order_is_right(pages, [75, 47, 61, 53, 29]), int)
        self.assertIsInstance(check_if_order_is_right(pages, [97, 61, 53, 29, 13]), int)
        self.assertIsInstance(check_if_order_is_right(pages, [75, 29, 13]), int)
        self.assertEqual(check_if_order_is_right(pages, [75, 47, 61, 53, 29]), 61)
        self.assertEqual(check_if_order_is_right(pages, [97, 61, 53, 29, 13]), 53)
        self.assertEqual(check_if_order_is_right(pages, [75, 29, 13]), 29)
        self.assertIsInstance(check_if_order_is_right(pages, [75, 97, 47, 61, 53]), tuple)
        self.assertIsInstance(check_if_order_is_right(pages, [61, 13, 29]), tuple)
        self.assertIsInstance(check_if_order_is_right(pages, [97, 13, 75, 29, 47]), tuple)

    def test_second_sample(self):
        self.assertEqual(change_order_position_to_right_format(pages, [75, 97, 47, 61, 53]), 47)
        self.assertEqual(change_order_position_to_right_format(pages, [61, 13, 29]), 29)
        self.assertEqual(change_order_position_to_right_format(pages, [97, 13, 75, 29, 47]), 47)

if __name__ == "__main__":
    unittest.main()