# define main function
def main():
    # Ask for user input, remove whitespaces and convert to lower case
    greeting = input("Greeting: ").strip().lower()
    # If greeting start with hello
    if greeting.startswith("hello"):
        print("$0")
    # If greeting start with h
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
