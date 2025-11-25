import random
import string

def create_password(length=12, include_upper=True, include_lower=True,
                    include_digits=True, include_symbols=True,
                    exclude_similar=False):
    
    chars = ""
    similar = "l1I0Oo"

    if include_upper:
        chars += string.ascii_uppercase
    if include_lower:
        chars += string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += "!@#$%^&*()-_=+[]{}<>?/"

    if exclude_similar:
        chars = "".join(c for c in chars if c not in similar)

    if not chars:
        return "Error: No character types selected."

    return "".join(random.choice(chars) for _ in range(length))


def main():
    print("Simple Password Generator")

    length = int(input("Password length: "))
    include_upper = input("Include uppercase (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase (y/n): ").lower() == 'y'
    include_digits = input("Include digits (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols (y/n): ").lower() == 'y'
    exclude_similar = input("Exclude similar characters (y/n): ").lower() == 'y'

    password = create_password(length, include_upper, include_lower,
                               include_digits, include_symbols, exclude_similar)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()

