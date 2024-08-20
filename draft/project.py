import cowsay

cowsay.beavis("Welcome to CS50!")


def main():
    text = "Login = 1\nCreate Account = 2\nPlease enter 1 or 2: "
    try:
        choice = int(input(text))
        if choice == 1:
            print("Login Initiated")
            print(login())
        elif choice == 2:
            print("Account Creation Initiated")
            print(create_account())
        else:
            sys.exit("Invalid Options")
    except ValueError:
        sys.exit("Invalid Options")
