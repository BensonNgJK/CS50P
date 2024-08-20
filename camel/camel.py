def main():
    # Ask user for input in camelCase
    camel = input("CamelCase: ")
    print("snake_case:", convert(camel))

# Function to convert from camelCase to snake_case
def convert(text):
    for i in text:
        if i.isupper():
            text = text.replace(i, f"_{i.lower()}")
    return text

main()
