# Import relavent libraries/functions
import sys
import csv


# define function to validate the command-line arguments
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            try:
                convert(sys.argv[1])
            except FileNotFoundError:
                sys.exit(f"Could not read {sys.argv[1]}")
        else:
            sys.exit("Not a CSV file")


# function to convert each row to desire format
def convert(input):
    with open(input) as before_csv, open(sys.argv[2], "w") as after_csv:
        reader = csv.DictReader(before_csv)
        writer = csv.DictWriter(after_csv, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(sep=", ")
            house = row["house"]
            writer.writerow({"first": first, "last": last, "house": house})


# Run main function within the program
if __name__ == "__main__":
    main()
