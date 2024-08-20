# Define main function
def main():
    namelist = names("Name: ")
    adieu_join(namelist)


# Define function to ask user for input and store input in a list
def names(prompt):
    namelist = []
    while True:
        try:
            name = input(prompt)
            namelist.append(name)
        except EOFError:
            print("", end="\n")
            return namelist


# Define function to join names according to desire formating (Liesl, Friedrich, and Louisa)
def adieu_join(namelist):
    if len(namelist) == 1:
        print(f"Adieu, adieu, to {namelist[0]}")
    if len(namelist) == 2:
        print(f"Adieu, adieu, to {namelist[0]} and {namelist[1]}")
    if len(namelist) > 2:
        text = ""
        for _ in namelist[: (len(namelist) - 1)]:
            text += _ + ", "
        print(f"Adieu, adieu, to {text}and {namelist[len(namelist)-1]}")


# Run main function in the same file
if __name__ == "__main__":
    main()
