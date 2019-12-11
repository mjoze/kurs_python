import unittest
from fields import rectangle, triangle, trapeze


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 50

    def test_rectangle_with_correct_values(self):
        result = rectangle(self.a, self.b)
        self.assertEqual(result, 500)

    def test_rectangle_with_incorrect_value(self):
        with self.assertRaises(ValueError):
            rectangle(5, 'aaa')

    def test_triangle_with_correct_values(self):
        result = triangle(self.a, self.b)
        self.assertEqual(result, 250)

    def test_triangle_with_incorrect_value(self):
        with self.assertRaises(ValueError):
            triangle('sss', 3)

    def test_trapeze_with_correct_value(self):
        result = trapeze(10, 10, 2)
        self.assertEqual(result, 20)

    def test_trapeze_with_incorrect_value(self):
        with self.assertRaises(ValueError):
            trapeze(5, 'aaa')

    def tearDown(self):
        del self.a
        del self.b


if __name__ == '__main__':
    unittest.main()