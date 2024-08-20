# Create main function
def main():
    text = input("Input: ")
    print("Output: ", omit_vowels(text))

# Loop function to omit vowels
def omit_vowels(text):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        if vowel in text:
            text = text.replace(vowel, "")
    return text

main()

