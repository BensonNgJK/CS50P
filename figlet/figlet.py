# import sys which allow us to take input from the command-line
# import Figlet function from pyfiglet
import sys
from pyfiglet import Figlet
from random import choice

# define function which ensure valid input into command-line
def main():
    # Define figlet
    figlet = Figlet()
    # Save a list of available fonts
    fonts_list = figlet.getFonts()
    if len(sys.argv) == 1:
        text = input("Input: ")
        font = choice(fonts_list)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts_list:
        text = input("Input: ")
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
    font = figlet.setFont(font=font)
    print(figlet.renderText(text))

# Run main function within same file
if __name__ == "__main__":
    main()
