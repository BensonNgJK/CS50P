# define a main function which prints user inputs in snake case
def main():
    print(convert(input("camelCase: ")))

# function which converts camelCase to snakecase
def convert(camel):
    snake = ""
    for i in camel:
        if i.isupper():
            i = str("_") + i.lower()
            snake = snake + i
        else:
            i = str(i)
            snake = snake + i
    return snake

# Run program
main()

