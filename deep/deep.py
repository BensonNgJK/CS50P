# define main function
def main():
    # Ask for user input and convert string to lower case
    user_input = input("Pls provide input: ").lower().strip()
    # Match user input with valid answer and return yes/no
    match user_input:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()
