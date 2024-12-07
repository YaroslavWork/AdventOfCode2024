import unittest
from main import find_visit_by_guard_positions


class TestGetDistance(unittest.TestCase):
    def test_helper_function_get_true(self):
        objects = [
            (4, 0),
            (9, 1),
            (2, 3),
            (7, 4),
            (1, 6),
            (8, 7),
            (0, 8),
            (6, 9)
        ]
        guard = [4, 6]

        self.assertEqual(find_visit_by_guard_positions(10, 10, objects, guard), 41)


if __name__ == '__main__':
    unittest.main()