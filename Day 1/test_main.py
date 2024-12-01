import unittest
from main import get_distance

class TestGetDistance(unittest.TestCase):
    def test_first_sample(self):
        first_column = [3, 4, 2, 1, 3, 3]
        second_column = [4, 3, 5, 3, 9, 3]
        self.assertEqual(len(first_column), len(second_column))
        self.assertEqual(get_distance(first_column, second_column), 11)

if __name__ == "__main__":
    unittest.main()