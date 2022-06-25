from student_class import Student
import unittest


class TestStudent(unittest.TestCase):

    def test_full_name(self):

        std_1 = Student("Ghattamaneni", "Mahesh", "Babu")
        std_2 = Student("Nandamuri", "Taraka", "Ramarao")

        self.assertEqual(std_1.full_name(), "Ghattamaneni.Mahesh Babu")
        self.assertEqual(std_2.full_name(), "Nandamuri.Taraka Ramarao")

    def test_mail_id(self):

        std_1 = Student("Ghattamaneni", "Mahesh", "Babu")
        std_2 = Student("Nandamuri", "Taraka", "Ramarao")

        self.assertEqual(std_1.mail_id(), "Mahesh.Babu@gmail.com")
        self.assertEqual(std_2.mail_id(), "Taraka.Ramarao@gmail.com")


if __name__ == "__main__":
    unittest.main(verbosity=2)
