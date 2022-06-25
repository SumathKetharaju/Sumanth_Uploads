import unittest


class TestMultiplication(unittest.TestCase):

    def runTest(self):
        self.assertEqual(5 * 4, 20)


class TestAddition(unittest.TestCase):

    def runTest(self):
        self.assertEqual(5 + 4, 9)


class TestDivision(unittest.TestCase):

    def runTest(self):
        self.assertEqual(20 // 4,  5)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestMultiplication())
    suite.addTests([TestAddition(), TestDivision()])
    unittest.TextTestRunner().run(suite)
