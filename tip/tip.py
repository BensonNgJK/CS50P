def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove leading $ and convert input to float with 1 decimal
    d = float(d.removeprefix("$"))
    return d

def percent_to_float(p):
    # Remove trailing % and convert input to float
    p = float(p.removesuffix("%"))
    return p / 100


main()
