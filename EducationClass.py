from DateClass import Date


class EducationClass(Date):
    classroom = None
    teacher = None

    def write(self, string):
        try:
            buff = string.split()
            super().write_date(buff[0])
            self.classroom = buff[1]
            self.teacher = buff[2]
        except IndexError as error:
            print(f"Error: {repr(error)}")
            raise IndexError

    def print_class(self):
        print(".".join([str(self.year), str(self.month), str(self.day)]), self.classroom, self.teacher)

