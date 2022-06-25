import unittest


class TestList(unittest.TestCase):

    def test_list_index(self):
        sample_list = [2, 3, 5, 6, 8, 9]
        self.assertEqual(sample_list[-1], 9)
        self.assertNotEqual(sample_list[-2], 9)
        self.assertEqual(sample_list[1], 3)
        self.assertNotEqual(sample_list[2], 3)

    def test_list_slicing(self):
        sample_list = [2, 3, 5, 6, 8, 9]
        self.assertEqual(sample_list[1:3], [3, 5])
        self.assertNotEqual(sample_list[2:5], [1, 2, 3])
        self.assertEqual(sample_list[:-3], [2, 3, 5])
        self.assertNotEqual(sample_list[2:-4], [5, 6])


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite([TestList()])
    unittest.TextTestRunner().run(suite)


