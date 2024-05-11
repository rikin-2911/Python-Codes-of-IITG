import re

def check_username(username):
    # Check length
    if len(username) < 5:
        return False
    # Check for special characters or spaces
    if not re.match("^[a-zA-Z0-9_]+$", username):
        return False
    return True

def main():
    # Prompt user for username
    username = input("Enter a username: ")

    # Check if username meets criteria
    if check_username(username):
        print("Valid username.")
    else:
        print("Invalid username.")

if __name__ == "__main__":
    main()

