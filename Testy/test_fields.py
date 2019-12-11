import unittest
from fields import rectangle, triangle


class FieldsTestCase(unittest.TestCase):
    def test_rectangle_with_correct_values(self):
        result = rectangle(5, 5)
        self.assertEqual(result, 25)

    def test_triangle_with_correct_values(self):
        result = triangle(5, 5)
        self.assertEqual(result, 12.5)


if __name__ == '__main__':
    unittest.main()