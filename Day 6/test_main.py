import unittest
from main import find_visit_by_guard_positions, next_move, find_loops


class TestGuardsPos(unittest.TestCase):
    def test_helper_function_get_true(self):
        self.assertEqual(next_move(10, 10, [], [2, 1], 0), [2, 0, 0])
        self.assertEqual(next_move(10, 10, [], [2, 1], 1), [3, 1, 1])
        self.assertEqual(next_move(10, 10, [], [2, 1], 2), [2, 2, 2])
        self.assertEqual(next_move(10, 10, [], [2, 1], 3), [1, 1, 3])
        self.assertEqual(next_move(10, 10, [(2, 0)], [2, 1], 0), [2, 1, 1])
        self.assertEqual(next_move(10, 10, [(3, 1)], [2, 1], 1), [2, 1, 2])
        self.assertEqual(next_move(10, 10, [(2, 2)], [2, 1], 2), [2, 1, 3])
        self.assertEqual(next_move(10, 10, [(1, 1)], [2, 1], 3), [2, 1, 0])
        self.assertEqual(next_move(10, 10, [], [2, 0], 0), None)
        self.assertEqual(next_move(10, 10, [], [9, 1], 1), None)
        self.assertEqual(next_move(10, 10, [], [2, 9], 2), None)
        self.assertEqual(next_move(10, 10, [], [0, 1], 3), None)

    def test_first_sample(self):
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

    def test_second_sample(self):
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

        self.assertEqual(find_loops(10, 10, objects, guard), 6)


if __name__ == '__main__':
    unittest.main()