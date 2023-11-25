import unittest
import Functions
from EducationClass import EducationClass
from DateClass import Date


class PipiTestCase(unittest.TestCase):
    def test_file_format(self):
        self.assertRaises(ValueError, Functions.file_open, "TestFile.xml")

    def test_file_emptiness(self):
        self.assertRaises(Exception, Functions.file_open, "EmptyTestFile.txt")

    def test_date_correct_input(self):
        line_1 = "09.02"
        line_2 = "2003.00.114"
        date_obj = Date()
        with self.assertRaises(Exception):
            date_obj.check_date_correctness(line_1)
        with self.assertRaises(Exception):
            date_obj.check_date_correctness(line_2)

    def test_valid_classroom(self):
        line = "410"
        ed_obj = EducationClass()
        with self.assertRaises(Exception):
            ed_obj.valid_classroom(line)

    def test_valid_teacher(self):
        line = "Bibi.A"
        ed_obj = EducationClass()
        with self.assertRaises(Exception):
            ed_obj.valid_teacher(line)

    def test_obj_init(self):
        none_obj = None
        lines = ["2003.09.03 4-12 Bizhik.A.V.", "2003.09.03 4-12 Alekseev.Q.T."]
        with self.assertRaises(TypeError):
            Functions.list_of_objects(none_obj, lines)

    def test_print_entire_schedule(self):
        obj_list = [None, None]
        list = []
        self.assertRaises(AttributeError, Functions.print_entire_schedule, obj_list)
        self.assertRaises(Exception, Functions.print_entire_schedule, list)


if __name__ == '__main__':
    unittest.main()
