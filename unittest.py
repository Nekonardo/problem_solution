import unittest

from task_a_steps_calculation import value_at_n, steps_to_reach_repeating
from task_c_steps_calculation_optimized import steps_to_reach_repeating_optimized


class Test(unittest.TestCase):
    # Task A
    def test_value_at_n(self):
        # test for valid input
        self.assertEqual(value_at_n(1, 1), 1)
        self.assertEqual(value_at_n(2, 1), 4)
        self.assertEqual(value_at_n(4, 1), 1)
        self.assertEqual(value_at_n(8, 1), 4)

        self.assertEqual(value_at_n(1, 2), 2)
        self.assertEqual(value_at_n(2, 2), 1)
        self.assertEqual(value_at_n(4, 2), 2)
        self.assertEqual(value_at_n(8, 2), 1)

        self.assertEqual(value_at_n(1, 5), 5)
        self.assertEqual(value_at_n(2, 5), 16)
        self.assertEqual(value_at_n(4, 5), 4)
        self.assertEqual(value_at_n(8, 5), 2)
        # test for invalid input
        self.assertRaises(Exception, value_at_n, 0, 1)
        self.assertRaises(Exception, value_at_n, 1, 0)

    def test_steps_to_reach_repeating(self):
        self.assertEqual(steps_to_reach_repeating(1), 1)
        self.assertEqual(steps_to_reach_repeating(2), 2)
        self.assertEqual(steps_to_reach_repeating(3), 8)
        self.assertEqual(steps_to_reach_repeating(4), 3)
        self.assertEqual(steps_to_reach_repeating(5), 6)

    # Task B
    def test_original_method_and_optimized_method(self):
        n = 10000
        for i in range(1, n):
            self.assertEqual(steps_to_reach_repeating(i), steps_to_reach_repeating_optimized(i))

    # Task C
    def test_steps_to_reach_repeating_optimized(self):
        self.assertEqual(steps_to_reach_repeating_optimized(1), 1)
        self.assertEqual(steps_to_reach_repeating_optimized(2), 2)
        self.assertEqual(steps_to_reach_repeating_optimized(3), 8)
        self.assertEqual(steps_to_reach_repeating_optimized(4), 3)
        self.assertEqual(steps_to_reach_repeating_optimized(5), 6)