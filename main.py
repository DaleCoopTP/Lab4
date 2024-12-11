import unittest
from rectangle import area


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_error_mul(self):
        res = area(3, 4)
        self.assertEqual(res, 15)


if __name__ == '__main__':
    unittest.main()
