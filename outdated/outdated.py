# define function which ask for inputs and convert valid inputs to YYYY-MM-DD
def main():
    while True:
        try:
            date = input("Date: ").strip()
            if ", " in date:
                mm, dd, yyyy = date.split(" ",2)
                mm = int(months.index(mm) + 1)
                dd = int(dd.replace(",",""))
                if 1 <= dd <= 31:
                    print(f"{yyyy}-{mm:02}-{dd:02}")
                    break
            elif "/" in date:
                mm, dd, yyyy = date.split("/",2)
                mm = int(mm)
                dd = int(dd)
                if 1 <= mm <= 12 and 1 <= dd <= 31:
                    print(f"{yyyy}-{mm:02}-{dd:02}")
                    break
            else:
                pass
        except ValueError:
            pass

# List of months from Jan to Dec
months = [
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

main()









