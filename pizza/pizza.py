# import revalent libraries/functions
import sys
import csv
from tabulate import tabulate

# define main function
def main():
    print(valid())

# define function to validate command-line argument
def valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].lower().endswith(".csv"):
            try:
                return convert(sys.argv[1])
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")

def convert(file_name):
    with open(file_name) as file:
        reader = list(csv.reader(file)) # Convert the file provided to a list
        return tabulate(reader[1:], headers = reader[0], tablefmt="grid")

if __name__ == "__main__":
    main()
