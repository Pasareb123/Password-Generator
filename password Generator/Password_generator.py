import random

letters = ["A","B","C","D","E","F","G","H","I","J","K","L",
           "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
           "a","b","c","d","e","f","g","h","i","j","k","l",
           "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

numbers = ["0","1","2","3","4","5","6","7","8","9"]

symbols = ["!","@","#","$","%","&","*","?","/","-","+"]

similar_chars = ["l","1","I","0","O","o"]

print("Welcome to  Password Generator")

length = int(input("How long do you want your password to be? "))

include_letters = input("Include letters? (y/n) ").lower() == "y"
include_numbers = input("Include numbers? (y/n) ").lower() == "y"
include_symbols = input("Include symbols? (y/n) ").lower() == "y"
exclude_similar = input("Exclude similar-looking characters (l,1,I,0,O,o)? (y/n) ").lower() == "y"

character_pool = []

if include_letters:
    character_pool += letters
if include_numbers:
    character_pool += numbers
if include_symbols:
    character_pool += symbols

if exclude_similar:
    character_pool = [c for c in character_pool if c not in similar_chars]

if len(character_pool) == 0:
    print("Error: No characters available to generate a password.")
else:
    password_list = []

    for _ in range(length):
        password_list.append(random.choice(character_pool))

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print("\nGenerated Password:")
    print(password)
