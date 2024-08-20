def main():
    user_input = input("Input: ")
    split(user_input," ")

# Create function to split a string of words
def split(text,delim):
    words = []
    word = ""
    for _ in text:
        if _ != delim:
            word += _
        else:
            words.append(word)
            word = ""
    words.append(word)
    print(words)

# run main function in same file
if __name__ == "__main__":
    main()
