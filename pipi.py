from collections import namedtuple
with open('pupu.txt', 'r') as file:
    lines = file.readlines()


class Date:
    def __init__(self, date):
        self.date = date


class EducationClass:
    def __init__(self, classroom, teacher, date: Date):
        self.classroom = classroom
        self.teacher = teacher
        self.date = date


def list_of_objects(obj, lines) -> list:
    day_list = []
    for string in lines:
        buff = string.split()
        ed_class = obj(buff[0], buff[1], buff[2])
        day_list.append(ed_class)
    return day_list


def print_entire_schedule(list):
    for elem in list:
        print(elem.classroom, elem.teacher, elem.date)


if __name__ == '__main__':
    print_entire_schedule(list_of_objects(EducationClass, lines))
