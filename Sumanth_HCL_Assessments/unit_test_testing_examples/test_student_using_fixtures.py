from student_class import Student
import unittest


class TestStudentFixture(unittest.TestCase):

    def setUp(self):
        print(f"Now I am in Setup Method")
        self.std_1 = Student("Ghattamaneni", "Mahesh", "Babu")
        self.std_2 = Student("Nandamuri", "Taraka", "Ramarao")

    def test_full_name_in_setup(self):
        print(f"Now I am in test_full_name_in_setup Method")
        self.assertEqual(self.std_1.full_name(), "Ghattamaneni.Mahesh Babu")
        self.assertEqual(self.std_2.full_name(), "Nandamuri.Taraka Ramarao")

    def test_mail_id_in_setup(self):
        print(f"Now I am in test_mail_id_in_setup Method")
        self.assertEqual(self.std_1.mail_id(), "Mahesh.Babu@gmail.com")
        self.assertEqual(self.std_2.mail_id(), "Taraka.Ramarao@gmail.com")

    def tearDown(self):
        print(f"Now I am in tearDown Method")


if __name__ == "__main__":
    unittest.main(verbosity=2)
