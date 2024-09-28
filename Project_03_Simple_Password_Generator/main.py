import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError("Password length must be a positive number.")

            use_letters = get_yes_no_input("Include letters? (y/n): ")
            use_numbers = get_yes_no_input("Include numbers? (y/n): ")
            use_symbols = get_yes_no_input("Include symbols? (y/n): ")

            if not (use_letters or use_numbers or use_symbols):
                print("Error: You must select at least one character set.")
                continue

            password = generate_password(length, use_letters, use_numbers, use_symbols)
            print(f"\nGenerated Password: {password}")

            generate_another = get_yes_no_input("\nGenerate another password? (y/n): ")
            if not generate_another:
                print("Thank you for using the Password Generator. Goodbye!")
                break

        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")

if __name__ == "__main__":
    main()