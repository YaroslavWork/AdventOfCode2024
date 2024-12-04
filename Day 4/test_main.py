import unittest
from main import word_search, check_word_normally_and_reverse

class TestGetDistance(unittest.TestCase):
    def test_helper_function_get_true(self):
        self.assertTrue(check_word_normally_and_reverse("XMAS", "XMAS"))
        self.assertTrue(check_word_normally_and_reverse("SAMX", "XMAS"))

    def test_helper_function_get_false(self):
        self.assertFalse(check_word_normally_and_reverse("", "XMAS"))
        self.assertFalse(check_word_normally_and_reverse("XNAS", "XMAS"))

    def test_first_sample(self):
        words = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ]
        self.assertEqual(word_search(words), 18)
    

if __name__ == "__main__":
    unittest.main()