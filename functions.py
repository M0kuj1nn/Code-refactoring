"""memory_profiler"""
from memory_profiler import profile


@profile
def file_open(data_file):
    """Open file and return lines"""
    with open(data_file, 'r', encoding='UTF-8') as file:
        if not data_file.endswith(".txt"):
            raise ValueError("Error: file must have .txt extension")
        lines = file.readlines()
        file.close()
        if len(lines) == 0:
            raise TypeError("Error: file must not be empty")
        return lines


@profile
def list_of_objects(obj, lines) -> list:
    """Fill object by lines"""
    day_list = []
    try:
        for string in lines:
            ed_class = obj()
            ed_class.read(string)
            day_list.append(ed_class)
        return day_list
    except TypeError as error:
        print(f"Error: {repr(error)}")
        raise TypeError from error


@profile
def print_entire_schedule(lst):
    """Function for print schedule"""
    try:
        if len(lst) == 0:
            raise TypeError("Error: list must be field")
        for elem in lst:
            elem.print_class()
    except AttributeError as error:
        print(f"Error: {repr(error)}")
        raise AttributeError from error
