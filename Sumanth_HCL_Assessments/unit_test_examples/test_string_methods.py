import unittest


class StringMethods(unittest.TestCase):

    def test_capital(self):
        self.assertEqual("sasi".capitalize(), "Sasi")

    def test_boolean(self):
        a = True
        b = False
        self.assertNotEqual(a, b)

    def test_is_digit(self):
        self.assertTrue("894".isdigit())


if __name__ == "__main__":
    unittest.main()

