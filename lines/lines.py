# import relavent libraries/functions
import sys

def main():
    print(f"{valid()}")

# define function to ensure valid command-line argument
def valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].lower().endswith(".py"):
            try:
                with open(sys.argv[1]) as file:
                    return count_lines(file)
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a Python file")

def count_lines(file):
    count = 0
    for line in file:
        if line.strip().startswith("#") or line.strip() == "":
            pass
        else:
            count += 1
    return count

# Run main function if in the same program
if __name__ == "__main__":
    main()
