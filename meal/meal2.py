# Main function to print meal time given the time input
def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# Convert time from string to float
def convert(time):
    hour, min = time.split(":")
    return float(hour) + float(min)/60

# Call main function
if __name__ == "__main__":
    main()
