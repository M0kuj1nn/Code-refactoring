import unittest
import Functions
from EducationClass import EducationClass


class PipiTestCase(unittest.TestCase):
    def test_file_format(self):
        self.assertRaises(ValueError, Functions.file_open, "TestFile.xml")

    def test_file_emptiness(self):
        self.assertRaises(Exception, Functions.file_open, "EmptyTestFile.txt")

    def test_date_correct_input(self):
        lines = [".02 4-06 Bizhik.A.V.", "2003.03 4-12 Alekseev.Q.T."]
        with self.assertRaises(Exception):
            Functions.list_of_objects(EducationClass, lines)

    def test_list_lines(self):
        lines = ["2003.02.09 Bizhik.A.V.", "2003.09.03 4-12"]
        with self.assertRaises(IndexError):
            Functions.list_of_objects(EducationClass, lines)

    def test_obj_init(self):
        class TestClass:
            def __init__(self, a, b, c, d):
                self.a = a
                self.b = b
                self.c = c
                self.d = d

        lines = ["2003.09.03 4-12 Bizhik.A.V.", "2003.09.03 4-12 Alekseev.Q.T."]
        with self.assertRaises(TypeError):
            Functions.list_of_objects(TestClass, lines)

    def test_print_entire_schedule(self):
        obj = None

        class TestClass:
            def __init__(self):
                self.year = "2003"
                self.month = "10"
                self.classroom = "3-03"
                self.teacher = "Sasha Grey"
        list_obj = [TestClass() for _ in range(3)]

        self.assertRaises(TypeError, Functions.print_entire_schedule, obj)
        self.assertRaises(AttributeError, Functions.print_entire_schedule, list_obj)


if __name__ == '__main__':
    unittest.main()
