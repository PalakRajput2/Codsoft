import random
import string

def generate_password(length):
    # Character sets
    letters = string.ascii_letters   # Contains both lowercase and uppercase
    digits = string.digits           # Contains '0123456789'
    special_chars = "!@#$%^&*()-_=+"

    # Combine all character sets
    available_chars = letters + digits + special_chars

    # Generate a random password
    password = ''.join(random.choice(available_chars) for _ in range(length))
    return password

def main():
    # User input: Desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            raise ValueError("The length must be at least 1.")
    except ValueError as e:
        print("Invalid input. Please enter a valid integer for the password length.")
        return
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
