import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^([1-9]|1[0-2])(:[0-5]\d)? ([AP]M) to ([1-9]|1[0-2])(:[0-5]\d)? ([AP]M)$",
                         s,
                         re.IGNORECASE
    ):
        hr_start = convert_hr(time.group(3),time.group(1))
        hr_end = convert_hr(time.group(6),time.group(4))
        min_start = convert_min(time.group(2))
        min_end = convert_min(time.group(5))
        return f"{hr_start:02}{min_start} to {hr_end:02}{min_end}"
    else:
        raise ValueError

def convert_hr(ampm,hr):
    if ampm == "PM" and int(hr) != 12:
        return int(hr) + 12
    elif ampm == "AM" and int(hr) == 12:
        return int(0)
    else:
        return int(hr)

def convert_min(min):
    if min == None:
        return ":00"
    else:
        return min

if __name__ == "__main__":
    main()
