import sys
import re
import inflect
from datetime import date

p = inflect.engine()
def main():
    birth_date = input("Date of Birth: ")
    dob=get_bd(birth_date)
    dob=change_to_words(dob[0],dob[1],dob[2])
    print(dob)
def change_to_words(day,month,year):
    try:
        date_of_birth = date(int(year),int(day), int(month))
        date_of_today=date.today()
        all_final=date_of_today-date_of_birth
        total_minutes = all_final.days * 24 * 60
        engin=p.number_to_words(total_minutes,andword="")
        all_final=engin.capitalize()+" minutes"
        return all_final
    except ValueError:
        sys.exit("Invalid date")
def get_bd(birth_date):
    if date := re.search(r"^(?:([0-9]{4})-([0-9]{2})-([0-9]{2}))$", birth_date):
        day = date.group(2)
        month = date.group(3)
        year = date.group(1)
        return day, month, year
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()