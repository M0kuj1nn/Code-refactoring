class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class EducationClass(Date):
    def __init__(self, year, month, day, classroom, teacher):
        super().__init__(year, month, day)
        self.classroom = classroom
        self.teacher = teacher
