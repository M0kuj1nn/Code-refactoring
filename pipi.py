from Classes import EducationClass
import Functions

if __name__ == '__main__':
    Functions.print_entire_schedule(
        Functions.list_of_objects(EducationClass, Functions.file_open('pupu.txt')))
