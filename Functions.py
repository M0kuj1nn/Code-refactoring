import re


def file_open(data_file):
    with open(data_file, 'r') as file:
        if not data_file.endswith(".txt"):
            raise ValueError("Error: file must have .txt extension")
        lines = file.readlines()
        file.close()
        if len(lines) == 0:
            raise Exception("Error: file must not be empty")
        return lines


def list_of_objects(obj, lines) -> list:
    day_list = []
    try:
        for string in lines:
            buff = string.split()
            date_pattern = r"\w+\.\w+\.\w+"
            match = re.match(date_pattern, buff[0])
            if not match:
                raise Exception("Error:The first word in the line must be a date at year.month.day format")
            date_elems = buff[0].split(".")
            ed_class = obj(date_elems[0], date_elems[1], date_elems[2], buff[1], buff[2])
            day_list.append(ed_class)
    except TypeError as error:
        print(f"Error: {repr(error)}")
        raise TypeError
    except IndexError as error:
        print(f"Error: {repr(error)}")
        raise IndexError
    else:
        return day_list


def print_entire_schedule(list):
    try:
        for elem in list:
            date = ".".join([str(elem.year), str(elem.month), str(elem.day)])
            print(date, elem.classroom, elem.teacher)
    except TypeError as error:
        print(f"Error: {repr(error)}")
        raise TypeError
    except AttributeError as error:
        print(f"Error: {repr(error)}")
        raise AttributeError
