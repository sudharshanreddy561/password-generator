# Password Generator Program by Sudharshan

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password

def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    password = generate_password(length)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
