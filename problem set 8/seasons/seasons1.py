import sys
import re
import inflect
from datetime import date
p = inflect.engine()
class Dateofbirth:
        def __init__(self,day,month,year):
            self.day=day
            self.month=month
            self.year=year
        def __str__(self):
            date_of_birth = date(int(self.year), int(self.month), int(self.day))
            date_of_today=date.today()
            all_final=date_of_today-date_of_birth
            total_minutes = all_final.days * 24 * 60
            engin=p.number_to_words(total_minutes,andword="")
            all_final=engin.capitalize()+" minutes"
            return f"{all_final}"
        @classmethod
        def get(cls):
            birth_date = input("Date of Birth: ")
            if date := re.search(r"^(?:([0-9]{4}|)-([0-9]{2})-([0-9]{2}))$", birth_date):
                day = date.group(2)
                month = date.group(3)
                year = date.group(1)
                return cls(day, month, year)
            else:
                sys.exit("Invalid date")
def main():
    dob = Dateofbirth.get()
    print(dob)

if __name__ == "__main__":
    main()
