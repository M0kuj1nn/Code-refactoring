from DateClass import Date


class EducationClass(Date):
    def __init__(self, year, month, day, classroom, teacher):
        super().__init__(year, month, day)
        self.classroom = classroom
        self.teacher = teacher
        self.date = None

    def date_join(self):
        self.date = ".".join([str(self.year), str(self.month), str(self.day)])

    def print_class(self):
        print(self.date, self.classroom, self.teacher)