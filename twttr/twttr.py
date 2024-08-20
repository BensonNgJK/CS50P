# define main function
def main():
    text = input("Input: ")
    convert(text)

# define function to omitted vowels
def convert(text):
    vowels = ["a", "e", "i", "o", "u"]
    for _ in text:
        if _.lower() in vowels:
            text = text.replace(_, "")
    print(f"Output: {text}")

main()
