import random
import string

def generate_password(length):
    # Define the characters to use in the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Ensure the password contains at least one of each type of character
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    # Fill the rest of the password length with random characters from all categories
    all_characters = lowercase + uppercase + digits
    password += random.choices(all_characters, k=length - 3)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Example usage
password_length = 10
password = generate_password(password_length)
print(f"Generated Password: {password}")
