import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area(self):
        a, b, c = 3, 4, 5

        result = area(a, b, c)

        self.assertEqual(result, 6)

    def test_perimeter(self):
        a, b, c = 3, 4, 5

        result = perimeter(a, b, c)

        self.assertEqual(result, 12)

    def test_negative_sides(self):
        a, b, c = -3, 4, 5

        with self.assertRaises(AssertionError):
            area(a, b, c)

    def test_invalid_triangle(self):
        a, b, c = 1, 1, 2

        with self.assertRaises(AssertionError):
            perimeter(a, b, c)
