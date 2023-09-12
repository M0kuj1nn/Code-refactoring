from collections import namedtuple
with open('pupu.txt', 'r') as file:
    lines = file.readlines()

Schedule = namedtuple('Schedule', 'type data classroom teacher')

day_list = []


def list_of_objects(obj, lines):
    for string in lines:
        buff = string.split()
        day = obj(buff[0], buff[1], buff[2], buff[3])
        day_list.append(day)


def print_entire_schedule():
    for elem in day_list:
        print(elem.type, elem.data, elem.classroom, elem.teacher)


if __name__ == '__main__':
    list_of_objects(Schedule, lines)
    print_entire_schedule()
