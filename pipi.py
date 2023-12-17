"""Main file"""
import cProfile
from educationclass import EducationClass
import functions


def main():
    """Main function"""
    functions.print_entire_schedule(
        functions.list_of_objects(EducationClass, functions.file_open('pupu.txt')))


if __name__ == '__main__':
    main()

cProfile.run("main()")












