from DateClass import Date


class EducationClass(Date):
    def __init__(self, year, month, day, classroom, teacher):
        super().__init__(year, month, day)
        self.classroom = classroom
        self.teacher = teacher

