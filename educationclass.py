"""Module for compare string with pattern"""
import re

from memory_profiler import profile

from dateclass import Date


class EducationClass:
    """Class with data about the teacher, room and date is stored"""
    date = Date()
    classroom = None
    teacher = None

    @profile
    def valid_classroom(self, classroom):
        """Сhecks audience input validity"""
        classroom_pattern = r'^\d+-\d+$'
        if not re.match(classroom_pattern, classroom):
            raise TypeError("Error:The classroom must be at number-number format")

    @profile
    def valid_teacher(self, teacher):
        """Сhecks teacher input validity"""
        teacher_pattern = r"[A-Z][a-z]+\.[A-Z]\.[A-Z]"
        if not re.match(teacher_pattern, teacher):
            raise TypeError("Error:The teacher must be at surname.initial.initial format")

    @profile
    def read(self, string):
        """Fill education class"""
        try:
            buff = string.split()
            self.date.read_date(buff[0])
            self.valid_classroom(buff[1])
            self.valid_teacher(buff[2])
            self.classroom = buff[1]
            self.teacher = buff[2]
        except IndexError as error:
            print(f"Error: {repr(error)}")
            raise RuntimeError from error

    @profile
    def print_class(self):
        """Print EducationClass"""
        print(self.date.date_join, self.classroom, self.teacher)
