# import required libraries/functions
from datetime import date
from datetime import timedelta
import inflect
import sys

# def main function
def main():
    p = inflect.engine()
    print(f"{p.number_to_words(convert(input("Date of Birth: ")), andword= "")} minutes".capitalize())

# def function to convert age to minutes
def convert(s):
    try:
        age = date.today() - date.fromisoformat(s)
        return int(age / timedelta(minutes=1))
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
