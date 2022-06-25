import unittest


class TestString(unittest.TestCase):

    def runTest(self):
        self.assertEqual("a" * 4, "aaaa")


class TestUpperCase(unittest.TestCase):

    def runTest(self):
        self.assertEqual("mahesh".upper(), "MAHESH")


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite([TestUpperCase(), TestString()])
    unittest.TextTestRunner().run(suite)

