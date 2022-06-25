import unittest
import find_areas


class TestingStrings(unittest.TestCase):

    def test_triangle(self):
        result = find_areas.triangle(10, 5)
        self.assertEqual(result, 25)

    def test_rectangle(self):
        self.assertEqual(find_areas.rectangle(6, 7), 42)

    def test_square(self):
        self.assertEqual(find_areas.square(6), 36)


if __name__ == "__main__":
    unittest.main()
