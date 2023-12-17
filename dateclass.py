"""Module for rematching text"""
import re

from memory_profiler import profile


class Date:
    """Date class with year, month, day, date_join fields"""
    year = None
    month = None
    day = None
    date_join = None

    @profile
    def check_date_correctness(self, date):
        """Checking input date correctness"""
        date_pattern = r"\w+\.\w+\.\w+"
        match = re.match(date_pattern, date)
        if not match:
            raise TypeError("Error:The first word in the line must be a "
                            "date at year.month.day format")
        date_elems = date.split(".")
        if 1 <= int(date_elems[1]) >= 12:
            raise TypeError("Error:Incorrect month input")
        if 1 <= int(date_elems[2]) >= 31:
            raise TypeError("Error:Incorrect day input")

    @profile
    def date_joining(self):
        """Join string for output"""
        self.date_join = ".".join([str(self.year), str(self.month), str(self.day)])

    @profile
    def read_date(self, date):
        """Fill Date class"""
        self.check_date_correctness(date)
        date_elems = date.split(".")
        self.year = date_elems[0]
        self.month = date_elems[1]
        self.day = date_elems[2]
        self.date_joining()
