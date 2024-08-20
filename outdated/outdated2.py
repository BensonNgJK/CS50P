"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

# list for months

months_list = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]

# get user inputs and verify inputs
def main():
  while True:
    try:
      i = str(input("Date: ")).strip()
      if i.count(" ") == 2 and i.count(", ") == 1:
        i = i.replace(",", "")
        month, day, year = i.split(sep = " ")
        if month in months_list:
          month = str(months_list.index(month) + 1)
        if month.isnumeric() and day.isnumeric() and year.isnumeric():
          month = int(month)
          day = int(day)
          year = int(year)
          if 1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999:
            print(f"{year:04}","-",f"{month:02}","-",f"{day:02}", sep="")
            break
      elif i.count("/") == 2:
        month, day, year = i.split(sep = "/")
        if month.isnumeric() and day.isnumeric() and year.isnumeric():
          month = int(month)
          day = int(day)
          year = int(year)
          if 1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999:
            print(f"{year:04}","-",f"{month:02}","-",f"{day:02}", sep="")
            break
      else:
        pass
    except ValueError:
      pass

main()
