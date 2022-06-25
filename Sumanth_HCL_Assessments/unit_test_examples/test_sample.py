import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("FOO".lower(), "foo")

    def test_lower(self):
        self.assertEqual("FOO".lower(), "foo")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_islower(self):
        self.assertTrue("foo".islower())
        self.assertFalse("fOo".islower())

    def test_split(self):
        input_string = "Mahesh Babu"
        self.assertEqual(input_string.split(), ["Mahesh", "Babu"])

        # with self.assertRaises(TypeError):
        #     input_string.split(2)


# if __name__ == "__main__":
#     unittest.main()
