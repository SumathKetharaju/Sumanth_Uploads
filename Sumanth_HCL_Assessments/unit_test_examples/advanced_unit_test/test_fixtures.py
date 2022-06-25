import unittest
from student_details import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        print("-------------------------------------- This is setUp method --------------------------------------")
        self.student_1 = Student("Nandamuri", "Ramarao", 25000)
        self.student_2 = Student("Konidela", "Charan", 28000)

    def tearDown(self):
        print("-------------------------------------- This is tearDown method --------------------------------------")

    def test_mail_id_in_setup(self):
        print("----------------------------------- This is test_mail_id_in_setup ---------------------------------")
        self.assertEqual(self.student_1.mail_id(), "Nandamuri.Ramarao@gmail.com")
        self.assertEqual(self.student_2.mail_id(), "Konidela.Charan@gmail.com")

        self.student_1.first_name = "Mahesh"
        self.student_2.first_name = "Prabhas"

        self.assertEqual(self.student_1.mail_id(), "Mahesh.Ramarao@gmail.com")
        self.assertEqual(self.student_2.mail_id(), "Prabhas.Charan@gmail.com")

    def test_full_name_in_setup(self):

        print("----------------------------------- This is test_full_name_in_setup ---------------------------------")
        self.assertEqual(self.student_1.full_name(), "Nandamuri Ramarao")
        self.assertEqual(self.student_2.full_name(), "Konidela Charan")

        self.student_1.first_name = "Mahesh"
        self.student_2.first_name = "Prabhas"

        self.assertEqual(self.student_1.full_name(), "Mahesh Ramarao")
        self.assertEqual(self.student_2.full_name(), "Prabhas Charan")

    def test_stipend_in_setup(self):

        print("----------------------------------- This is test_stipend_in_setup ---------------------------------")
        self.student_1.apply_hike()
        self.student_2.apply_hike()

        self.assertEqual(self.student_1.initial_stipend, 26250.0)
        self.assertEqual(self.student_2.initial_stipend, 29400.0)


if __name__ == "__main__":
    unittest.main()