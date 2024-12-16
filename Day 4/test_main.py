import unittest
from main import word_search, check_word_normally_and_reverse, find_x_mas, check_if_it_is_mas

class TestWordSearch(unittest.TestCase):
    def test_helper_function_get_true(self):
        self.assertTrue(check_word_normally_and_reverse("XMAS", "XMAS"))
        self.assertTrue(check_word_normally_and_reverse("SAMX", "XMAS"))

    def test_helper_function_get_false(self):
        self.assertFalse(check_word_normally_and_reverse("", "XMAS"))
        self.assertFalse(check_word_normally_and_reverse("XNAS", "XMAS"))

    def test_helper2_function_get_true(self):
        self.assertTrue(check_if_it_is_mas("M", "S"))
        self.assertTrue(check_if_it_is_mas("S", "M"))

    def test_helper_function_get_false(self):
        self.assertFalse(check_if_it_is_mas("X", "S"))
        self.assertFalse(check_if_it_is_mas("M", "M"))
        self.assertFalse(check_if_it_is_mas("S", "S"))
        self.assertFalse(check_if_it_is_mas("X", "M"))

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
    

    def test_second_sample(self):
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
        self.assertEqual(find_x_mas(words), 9)

if __name__ == "__main__":
    unittest.main()