# define main function
def main():
    while True:
        try:
            fraction = input("Fraction: ")
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            continue

# define function to ask user for valid input
def convert(fraction):
            try:
                x, y = fraction.split(sep="/")
                x = int(x)
                y = int(y)
                if y == 0:
                    raise ZeroDivisionError
                elif x > y:
                    raise ValueError
                else:
                    return round(x/y*100)
            except ValueError:
                 raise ValueError

# define function to return % or E or F
def gauge(percentage):
    if percentage >= 99:
        return f"F"
    elif percentage <= 1:
        return ("E")
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
