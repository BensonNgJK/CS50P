# "CS50" Registration & Login
#### Video Demo:  <https://youtu.be/s0ghjEze0O0>
#### Description:

The objective of this project is to create a registration and login page for "CS50." The program is designed to be practical and leverages the knowledge gained from the CS50P course while remaining simple enough to meet the final project requirements.

#### Registration:

In the registration process, the program allows users to "create an account" by prompting them for a valid email address (to be used as a username) and a secure password. The secure password must be at least 12 characters long and include a mix of upper and lower-case letters, numbers, and special characters. If both the username and password meet the specified requirements, they are saved in a CSV file. Following the CS50.ai advice, the program uses `bcrypt` to securely store the password.

This functionality is achieved using the following functions in `project.py`:

- **`valid_email(email)`**: Utilizes the `checkers.is_email` method from the `validator_collection` package to verify if the email address (case-insensitive) is valid. Additionally, it checks if the email address already exists in the `account.csv` file to prevent duplicate registrations. If the email is valid and unique, the function returns the email address in lowercase; otherwise, it raises a `ValueError` with a descriptive message.

- **`valid_pw(s)`**: Ensures that the password is at least 12 characters long using the `len()` function. It also employs the `re.search()` function with various regular expressions to verify that the password includes a mix of upper and lower-case letters, numbers, and special characters.

- **`create_account()`**: Allows users up to three attempts to create an account. If the username or password does not meet the requirements, the function provides an error message explaining the issue. If both the username and password are valid, the function saves them in the `account.csv` file, with the password hashed using `bcrypt.hashpw` to ensure secure storage.

#### Login:

During login, the program prompts the user for their username and password, verifies them against the existing database, and, upon successful login, displays a cow greeting the user with "Welcome to CS50!"

This functionality is achieved using the following functions in `project.py`:

- **`login()`**: Provides users with up to three attempts to log in to their account. If the username or password does not match the existing records in the `account.csv` file, it outputs "Invalid username and/or password." The function utilizes `valid_login(username, password)` to verify the credentials. The hashed password is verified using `bcrypt.checkpw`. Upon successful login, the function uses `cowsay` to display a cow greeting the user with "Welcome to CS50!"

As noted, the `hash_password()` and `verify_password()` functions utilize `bcrypt` to ensure that users' passwords are stored securely.

#### Main Function:

The `main()` function utilizes `argparse` to accept a command-line argument (`--login` or `--registration`), which initiates either the login or registration process.

#### Conclusion:

This project effectively applies the modules and concepts learned from CS50P to develop a practical and functional registration and login system. The `test_project.py` file includes comprehensive unit tests to verify the program's intended functionality. However, due to the scope of the course, functions like `create_account()` that involve saving data to a CSV file were not fully tested. Additionally, the code has been reformatted using `black` to enhance readability and maintain consistency.

#### Requirements:

The required libraries are listed in the `requirements.txt` file.
