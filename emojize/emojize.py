# Import function from library
import emoji

# Ask user for input and return emoji
def main():
    user_input = input("Input: ")
    print(emoji.emojize(f"Output: {user_input}", language = "alias"))

# Run main function if it is run in the program
if __name__ == "__main__":
    main()
