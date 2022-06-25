import unittest
import find_areas
import sys


class AssertsTesting(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)
        self.assertTrue((10 * 2) == 20)

    def test_assert_false(self):
        self.assertFalse(False)
        self.assertFalse((10 % 2) == 2)

    def test_equal(self):
        self.assertEqual(15, 3 * 5)

    def test_not_equal(self):
        self.assertNotEqual(10, 10 + 10)

    def test_perimeter(self):
        self.assertEqual(find_areas.get_perimeter(10, 5), 30)

    def test_value_error(self):
        self.assertRaises(ValueError, find_areas.get_perimeter, 10, 0)

    @unittest.skip("This Test is Temporarily Skipped")
    def test_value_error_using_with(self):
        with self.assertRaises(ValueError):
            find_areas.get_perimeter(10, 5)

    @unittest.skipIf(sys.version_info[0] >= 3, "This Test is also Temporarily Skipped")
    def test_value_error_using_skip_if(self):
        with self.assertRaises(ValueError):
            find_areas.get_perimeter(10, 5)

    @unittest.skipUnless(sys.platform.startswith("mac"), "Requires windows")
    def test_value_error_using_skip_unless(self):
        with self.assertRaises(ValueError):
            find_areas.get_perimeter(20, 5)


if __name__ == "__main__":
    unittest.main()

