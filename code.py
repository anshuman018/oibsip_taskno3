import argparse
import random
import string


def generate_random_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define a default character set containing all possible characters
    all_characters = ''
    if use_lowercase:
        all_characters += string.ascii_lowercase
    if use_uppercase:
        all_characters += string.ascii_uppercase
    if use_digits:
        all_characters += string.digits
    if use_special_chars:
        all_characters += string.punctuation

    # If no character sets are selected, include all by default
    if not any([use_lowercase, use_uppercase, use_digits, use_special_chars]):
        all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password with random characters
    if not all_characters:
        raise ValueError("No character set selected for password generation")

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument("--length", type=int, default=12, help="Password length")
    parser.add_argument("--lowercase", action="store_true", help="Include lowercase letters")
    parser.add_argument("--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("--digits", action="store_true", help="Include digits")
    parser.add_argument("--special-chars", action="store_true", help="Include special characters")
    parser.add_argument("--count", type=int, default=1, help="Number of passwords to generate")

    args = parser.parse_args()

    if args.length < 8:
        print("Error: Password length should be at least 8 characters")
    else:
        for i in range(args.count):
            random_password = generate_random_password(
                args.length,
                args.lowercase,
                args.uppercase,
                args.digits,
                args.special_chars
            )
            print(f"Random Password {i + 1}: {random_password}")
