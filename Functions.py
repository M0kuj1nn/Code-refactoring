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
            ed_class = obj()
            ed_class.write(string)
            day_list.append(ed_class)
        return day_list
    except TypeError as error:
        print(f"Error: {repr(error)}")
        raise TypeError


def print_entire_schedule(list):
    try:
        if len(list) == 0:
            raise Exception("Error: list must be field")
        for elem in list:
            elem.print_class()
    except AttributeError as error:
        print(f"Error: {repr(error)}")
        raise AttributeError
