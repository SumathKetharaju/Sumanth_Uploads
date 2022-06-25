import unittest


class TestingStrings(unittest.TestCase):

    def test_string(self):
        x = "Mahesh"
        y = "Mahesh"
        self.assertEqual(x, y)


if __name__ == "__main__":
    unittest.main()
