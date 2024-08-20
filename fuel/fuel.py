# define main function
def main():
    value = get_input("Fraction: ")
    percent(value)

# define function to ask user for valid input
def get_input(prompt):
    while True:
        try:
            x, y = input(prompt).split(sep="/")
            x = int(x)
            y = int(y)
            if x > y:
                pass
            else:
                return round(x/y*100)
        except (ValueError, ZeroDivisionError):
            pass

# define function to return % or E or F
def percent(value):
    if value >= 99:
        print("F")
    elif value <= 1:
        print("E")
    else:
        print(f"{value}%")

main()
