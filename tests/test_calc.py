import unittest
from calculate import calc
import math


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = [1]

        result = calc(fig, func, size)

        self.assertEqual(result, math.pi)

    def test_square_area(self):
        fig = 'square'
        func = 'area'
        size = [1]

        result = calc(fig, func, size)

        self.assertEqual(result, 1)

    def test_triangle_area(self):
        fig = 'triangle'
        func = 'area'
        size = [3, 4, 5]

        result = calc(fig, func, size)

        self.assertEqual(result, 6)

    def test_cirlce_perimeter(self):
        fig = 'circle'
        func = 'perimeter'
        size = [1]

        result = calc(fig, func, size)

        self.assertEqual(result, 2 * math.pi)

    def test_square_perimeter(self):
        fig = 'square'
        func = 'perimeter'
        size = [1]

        result = calc(fig, func, size)

        self.assertEqual(result, 4)

    def test_triangle_perimeter(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [3, 4, 5]

        result = calc(fig, func, size)

        self.assertEqual(result, 12)

    def test_invalid_fig(self):
        fig = 'invalid'
        func = 'perimeter'
        size = [3, 4, 5]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_func(self):
        fig = 'triangle'
        func = 'invalid'
        size = [3, 4, 5]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_size_count(self):
        fig = 'invalid'
        func = 'perimeter'
        size = [3, 4]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_negative_size(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [-3, 4, 5]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_triangle(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [3, 4, 100]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)
