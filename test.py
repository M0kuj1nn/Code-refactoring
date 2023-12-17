"""Unit tests"""
import unittest
import functions
from educationclass import EducationClass
from dateclass import Date


class PipiTestCase(unittest.TestCase):
    """Main test class"""
    def test_file_format(self):
        """Test file format"""
        self.assertRaises(ValueError, functions.file_open, "TestFile.xml")

    def test_file_emptiness(self):
        """Test file emptiness"""
        self.assertRaises(TypeError, functions.file_open, "EmptyTestFile.txt")

    def test_date_correct_input(self):
        """Test date correct input"""
        line_1 = "09.02"
        line_2 = "2003.00.114"
        date_obj = Date()
        with self.assertRaises(TypeError):
            date_obj.check_date_correctness(line_1)
        with self.assertRaises(TypeError):
            date_obj.check_date_correctness(line_2)

    def test_valid_classroom(self):
        """Test valid input of classroom"""
        line = "410"
        ed_obj = EducationClass()
        with self.assertRaises(TypeError):
            ed_obj.valid_classroom(line)

    def test_valid_teacher(self):
        """Test valid input of teacher"""
        line = "Bibi.A"
        ed_obj = EducationClass()
        with self.assertRaises(TypeError):
            ed_obj.valid_teacher(line)

    def test_obj_init(self):
        """Object initialization test"""
        none_obj = None
        lines = ["2003.09.03 4-12 Bizhik.A.V.", "2003.09.03 4-12 Alekseev.Q.T."]
        with self.assertRaises(TypeError):
            functions.list_of_objects(none_obj, lines)

    def test_print_entire_schedule(self):
        """Test for print_entire_schedule function"""
        obj_list = [None, None]
        lst = []
        self.assertRaises(AttributeError, functions.print_entire_schedule, obj_list)
        self.assertRaises(TypeError, functions.print_entire_schedule, lst)


if __name__ == '__main__':
    unittest.main()
