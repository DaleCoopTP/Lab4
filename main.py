import unittest
from rectangle import area


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_error_mul(self):  # Отрицательная величина
        res = area(-1, 4)
        self.assertEqual(res, "Error")

if __name__ == '__main__':
    unittest.main()
