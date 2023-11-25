import re


class Date:
    year = None
    month = None
    day = None

    def check_date_correctness(self, date):
        date_pattern = r"\w+\.\w+\.\w+"
        match = re.match(date_pattern, date)
        if not match:
            raise Exception("Error:The first word in the line must be a date at year.month.day format")
        date_elems = date.split(".")
        if 1 <= int(date_elems[1]) >= 12:
            raise Exception("Error:Incorrect month input")
        if 1 <= int(date_elems[2]) >= 31:
            raise Exception("Error:Incorrect day input")

    def read_date(self, date):
        self.check_date_correctness(date)
        date_elems = date.split(".")
        self.year = date_elems[0]
        self.month = date_elems[1]
        self.day = date_elems[2]