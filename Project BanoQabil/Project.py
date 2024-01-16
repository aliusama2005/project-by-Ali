import time
import getpass

# Dictionary to store user accounts
accounts = {}

# Function to create a new account
def create_account():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")

    # Store the account in the dictionary
    accounts[username] = password
    print("Account created successfully!")

# Function to test an account
def test_account():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Check if the account exists and the credentials are correct
    if username in accounts and accounts[username] == password:
        print("Welcome!")
    else:
        # Increment the failed attempts counter for the user
        if username in failed_attempts:
            failed_attempts[username] += 1
        else:
            failed_attempts[username] = 1

        # Check if the user has exceeded the maximum number of failed attempts
        if failed_attempts[username] > 5:
            print("Access denied! This account is locked for 30 seconds.")
            time.sleep(30)
            del failed_attempts[username]
        else:
            print("Access denied!")

# Initialize the failed attempts dictionary
failed_attempts = {}

# Main function
def main():
    while True:
        print("\n1. Create account")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            test_account()
        elif choice == 3:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()