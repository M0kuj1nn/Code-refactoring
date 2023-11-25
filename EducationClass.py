import re
from DateClass import Date


class EducationClass:
    date = Date()
    classroom = None
    teacher = None

    def valid_classroom(self, classroom):
        classroom_pattern = r'^\d+-\d+$'
        if not re.match(classroom_pattern, classroom):
            raise Exception("Error:The classroom must be at number-number format")

    def valid_teacher(self, teacher):
        teacher_pattern = r"[A-Z][a-z]+\.[A-Z]\.[A-Z]"
        if not re.match(teacher_pattern, teacher):
            raise Exception("Error:The teacher must be at surname.initial.initial format")

    def read(self, string):
        try:
            buff = string.split()
            self.date.read_date(buff[0])
            self.valid_classroom(buff[1])
            self.valid_teacher(buff[2])
            self.classroom = buff[1]
            self.teacher = buff[2]
        except IndexError as error:
            print(f"Error: {repr(error)}")
            raise RuntimeError

    def print_class(self):
        print(".".join([str(self.date.year), str(self.date.month), str(self.date.day)]), self.classroom, self.teacher)

