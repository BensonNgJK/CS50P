# Ask user for input
input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Convert inputs to string with lower case and strip
input = str(input).lower().strip()

# Print Yes if "42", otherwise print No
def answer():
    match input:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

answer()
