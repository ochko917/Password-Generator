import random
import string

def generate_password():
    print("=== Password Generator ===")
    
    upper = int(input("Number of uppercase letters: "))
    lower = int(input("Number of lowercase letters: "))
    digit = int(input("Numbers: "))
    symbol = int(input("Number of special characters: "))

    upper_chars = random.choices(string.ascii_uppercase, k=upper)
    lower_chars = random.choices(string.ascii_lowercase, k=lower)
    digit_num = random.choices(string.digits, k=digit)
    symbol_num = random.choices(string.punctuation, k=symbol)

    passlist = upper_chars + lower_chars + digit_num + symbol_num
    random.shuffle(passlist)

    password = ''.join(passlist)
    print(f"Generated Password: {password}")

generate_password()

