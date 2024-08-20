# define main function
def main():
    text = input("Input: ")
    print("Output:", shorten(text))

# define function to omitted vowels
def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    for _ in word:
        if _.lower() in vowels:
            word = word.replace(_, "")
    return f"{word}"

if __name__ == "__main__":
    main()
