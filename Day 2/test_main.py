import unittest
from main import check_if_code_is_safe

class TestCodeVerification(unittest.TestCase):
    def test_first_sample(self):
        samples = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]
        
        self.assertEqual(check_if_code_is_safe(samples[0]), True)
        self.assertEqual(check_if_code_is_safe(samples[1]), False)
        self.assertEqual(check_if_code_is_safe(samples[2]), False)
        self.assertEqual(check_if_code_is_safe(samples[3]), False)
        self.assertEqual(check_if_code_is_safe(samples[4]), False)
        self.assertEqual(check_if_code_is_safe(samples[5]), True)

if __name__ == "__main__":
    unittest.main()