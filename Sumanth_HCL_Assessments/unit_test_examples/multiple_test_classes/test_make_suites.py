import unittest


class TestMul(unittest.TestCase):

    def runTest(self):
        self.assertEqual(5 * 4, 20)


class TestAdd(unittest.TestCase):

    def runTest(self):
        self.assertEqual(5 + 4, 9)


class TestDiv(unittest.TestCase):

    def runTest(self):
        self.assertEqual(20 // 4,  5)


class SimpleTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertEqual(2, 2)

    def test_3(self):
        self.assertEqual(3, 3)

    def test_4(self):
        self.assertEqual(4, 4)


if __name__ == "__main__":
    # suite = unittest.TestSuite([TestDiv(), TestAdd()])
    # suite.addTest(TestMul())
    suite = unittest.makeSuite(SimpleTest, "test")
    suite.addTests([TestMul(), TestDiv(), TestAdd()])
    unittest.TextTestRunner().run(suite)
