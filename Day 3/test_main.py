import unittest
from main import find_a_mul_sequence_and_return_sum, find_a_mul_sequence_with_access_and_return_sum

class TestGetDistance(unittest.TestCase):
    def test_first_sample(self):
        sequence = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(find_a_mul_sequence_and_return_sum(sequence), 161)

    def test_second_sample(self):
        sequence = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        self.assertEqual(find_a_mul_sequence_with_access_and_return_sum(sequence), 48)
    

if __name__ == "__main__":
    unittest.main()