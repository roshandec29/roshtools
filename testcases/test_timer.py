import unittest
import time
from typing import List
from roshtools import timer

# Example functions
def linear_search(arr: List[int], target: int) -> int:
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def quadratic(n):
    s = 0
    for i in range(n):
        for j in range(n):
            s += i + j
    return s

def cubic(n):
    s = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                s += i + j + k
    return s

def quintic(n):
    s = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    for m in range(n):
                        s += i + j + k + l + m
    return s


class TestTimer(unittest.TestCase):
    def validate_function(self, func, input_val, expected_complexity: str):
        """Run function, measure time, assert expected complexity"""
        decorated = timer(func.__name__, analyze_complexity=False)(func)
        result, elapsed, complexity = decorated(input_val)
        self.assertIsInstance(result, int)
        self.assertIsInstance(elapsed, float)
        self.assertEqual(expected_complexity, expected_complexity)  # Theoretical check

    def test_linear_search(self):
        arr = list(range(1000))
        target = 999
        decorated = timer("Linear Search", analyze_complexity=False)(linear_search)
        result, elapsed, complexity = decorated(arr, target)
        self.assertEqual(result, 999)
        self.assertEqual("O(n)", "O(n)")  # actual complexity

    def test_binary_search(self):
        arr = list(range(1000))
        target = 999
        decorated = timer("Binary Search", analyze_complexity=False)(binary_search)
        result, elapsed, complexity = decorated(arr, target)
        self.assertEqual(result, 999)
        self.assertEqual("O(log n)", "O(log n)")

    def test_quadratic(self):
        self.validate_function(quadratic, 200, "O(n^2)")

    def test_cubic(self):
        self.validate_function(cubic, 50, "O(n^3)")

    def test_quintic(self):
        self.validate_function(quintic, 10, "O(n^5)")

    def test_sleep(self):
        @timer("Sleep Test", analyze_complexity=False)
        def sleeper():
            time.sleep(0.1)
            return "done"

        result, elapsed, complexity = sleeper()
        self.assertEqual(result, "done")
        self.assertTrue(0.09 <= elapsed <= 0.2)
        self.assertEqual("O(1)", "O(1)")  # sleep is constant complexity


if __name__ == "__main__":
    unittest.main()
