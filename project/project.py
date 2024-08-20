# import required libraries/functions
import sys
import argparse
import re
import csv
from validator_collection import validators, checkers
import cowsay
import bcrypt


# define main function
def main():
    parser = argparse.ArgumentParser(description="Login or Registration for CS50")
    parser.add_argument("--login", action="store_true", help=" User Login Option")
    parser.add_argument("--register", action="store_true", help="User Register Option")
    args = parser.parse_args()
    if args.login:
        print("Login Initiated")
        print(login())
    elif args.register:
        print("Account Creation Initiated")
        print(create_account())


# Validate email address when creating account
def valid_email(email):
    if checkers.is_email(email.lower()):
        with open("accounts.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if email.lower() == row["username"]:
                    raise ValueError("Email is already registered.")
        return email.lower()
    else:
        raise ValueError("Invalid email.")


# Validate password requirements when creating account
def valid_pw(s):
    if (
        len(s) >= 12
        and re.search(r"\d", s)
        and re.search(r"[A-Z]", s)
        and re.search(r"[a-z]", s)
        and re.search(r"[^A-Za-z0-9]", s)
    ):
        return s
    else:
        raise ValueError("Password does not meet requirements.")


# Save valid username/password into a csv file
def create_account():
    attempts = 1
    while True:
        try:
            username = valid_email(input("Email: "))
            password = valid_pw(input("Password: "))
            with open("accounts.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["username", "password"])
                hashed_password = hash_password(password)
                writer.writerow(
                    {"username": username, "password": hashed_password.decode()}
                )
                return "Account Created."
        except ValueError as e:
            if attempts < 3:
                attempts += 1
                print(e)
            else:
                print(e)
                sys.exit("Too many attempts. Please try again later.")


# Account login function
def login():
    attempts = 1
    while True:
        try:
            username = validators.email(input("Email: "))
            password = input("Password: ")
            return valid_login(username, password)
        except ValueError as e:
            if attempts < 3:
                attempts += 1
                print(e)
            else:
                print(e)
                sys.exit("Too many attempts. Please try again later.")


# Validate if account is valid with correct password
def valid_login(username, password):
    with open("accounts.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username.lower() == row["username"] and verify_password(
                row["password"], password
            ):
                return cowsay.get_output_string("cow", "Welcome to CS50!")
            else:
                continue
        raise ValueError("Invalid username and/or password.")


# Using bcrypt to hash the password before storing
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


# Using bcrypt to verify the provided password
def verify_password(stored_pw, provided_pw):
    return bcrypt.checkpw(provided_pw.encode(), stored_pw.encode())


# Run main function within file
if __name__ == "__main__":
    main()
