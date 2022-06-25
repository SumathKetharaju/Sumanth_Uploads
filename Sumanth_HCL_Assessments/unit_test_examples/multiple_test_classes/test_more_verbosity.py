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
    suite = unittest.makeSuite(SimpleTest, "test")
    suite.addTests([TestMul(), TestDiv(), TestAdd()])
    final_result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(f"Errors are --> {final_result.errors}")
    print(f"\nFailed test cases are --> {final_result.failures}")
    print(f"\nskipped test cases  are --> {final_result.skipped}")
    print(f"\nNumber of tests are --> {final_result.testsRun}")
    print(f"\nWas it a Successful test --> {final_result.wasSuccessful()}")
