import unittest
from student_details import Student


class TestStudent(unittest.TestCase):

    def test_mail(self):

        student_1 = Student("Taraka", "Ramarao", 25000)
        student_2 = Student("Ram", "Charan", 28000)

        self.assertEqual(student_1.mail_id(), "Taraka.Ramarao@gmail.com")
        self.assertEqual(student_2.mail_id(), "Ram.Charan@gmail.com")

        student_1.first_name = "Mahesh"
        student_2.first_name = "Prabhas"

        self.assertEqual(student_1.mail_id(), "Mahesh.Ramarao@gmail.com")
        self.assertEqual(student_2.mail_id(), "Prabhas.Charan@gmail.com")

    def test_full_name(self):
        student_1 = Student("Taraka", "Ramarao", 25000)
        student_2 = Student("Ram", "Charan", 28000)

        self.assertEqual(student_1.full_name(), "Taraka Ramarao")
        self.assertEqual(student_2.full_name(), "Ram Charan")

        student_1.first_name = "Mahesh"
        student_2.first_name = "Prabhas"

        self.assertEqual(student_1.full_name(), "Mahesh Ramarao")
        self.assertEqual(student_2.full_name(), "Prabhas Charan")

    def test_stipend(self):
        student_1 = Student("Taraka", "Ramarao", 25000)
        student_2 = Student("Ram", "Charan", 28000)

        student_1.apply_hike()
        student_2.apply_hike()

        self.assertEqual(student_1.initial_stipend, 26250.0)
        self.assertEqual(student_2.initial_stipend, 29400.0)


if __name__ == "__main__":
    unittest.main()

