import unittest
from main import can_made_this_euqation, can_made_this_euqation2, next_possibilities

class TestCalibrationProcess(unittest.TestCase):
    def test_helper_function_get_true(self):
        self.assertEqual(next_possibilities([0, 0, 0], 2), [0, 0, 1])
        self.assertEqual(next_possibilities([0, 0, 1], 2), [0, 1, 0])
        self.assertEqual(next_possibilities([0, 1, 1], 2), [1, 0, 0])
        self.assertEqual(next_possibilities([0, 0, 1], 3), [0, 0, 2])
        self.assertEqual(next_possibilities([0, 2, 2], 3), [1, 0, 0])
        self.assertEqual(next_possibilities([0, 2, 0], 3), [0, 2, 1])
        self.assertEqual(next_possibilities([2, 2, 2], 3), [0, 0, 0])

    def test_first_sample(self):
        equation = [
            [10, 19],
            [81, 40, 27],
            [17, 5],
            [15, 6],
            [6, 8, 6, 15],
            [16, 10, 13],
            [17, 8, 14],
            [9, 7, 18, 13],
            [11, 6, 16, 20]
        ]
        self.assertEqual(can_made_this_euqation(equation[0], 190), True)
        self.assertEqual(can_made_this_euqation(equation[1], 3_267), True)
        self.assertEqual(can_made_this_euqation(equation[2], 83), False)
        self.assertEqual(can_made_this_euqation(equation[3], 156), False)
        self.assertEqual(can_made_this_euqation(equation[4], 7_290), False)
        self.assertEqual(can_made_this_euqation(equation[5], 161_011), False)
        self.assertEqual(can_made_this_euqation(equation[6], 192), False)
        self.assertEqual(can_made_this_euqation(equation[7], 21_037), False)
        self.assertEqual(can_made_this_euqation(equation[8], 292), True)

    def test_second_sample(self):
        equation = [
            [10, 19],
            [81, 40, 27],
            [17, 5],
            [15, 6],
            [6, 8, 6, 15],
            [16, 10, 13],
            [17, 8, 14],
            [9, 7, 18, 13],
            [11, 6, 16, 20]
        ]
        self.assertEqual(can_made_this_euqation2(equation[0], 190), True)
        self.assertEqual(can_made_this_euqation2(equation[1], 3_267), True)
        self.assertEqual(can_made_this_euqation2(equation[2], 83), False)
        self.assertEqual(can_made_this_euqation2(equation[3], 156), True)
        self.assertEqual(can_made_this_euqation2(equation[4], 7_290), True)
        self.assertEqual(can_made_this_euqation2(equation[5], 161_011), False)
        self.assertEqual(can_made_this_euqation2(equation[6], 192), True)
        self.assertEqual(can_made_this_euqation2(equation[7], 21_037), False)
        self.assertEqual(can_made_this_euqation2(equation[8], 292), True)

if __name__ == '__main__':
    unittest.main()
        