# import validator
from validator_collection import checkers

# define main function
def main():
    print(valid(input("What's your email address? ")))

# define function to validate if input is valid email
def valid(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
