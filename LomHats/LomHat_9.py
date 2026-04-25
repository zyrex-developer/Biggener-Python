import string

special_chars = string.punctuation   # keep this as a string

while True:
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False  # this is boolean

    password = input('Enter your password: ')

    if len(password) < 8:
        print('Error: Password must be at least 8 characters long.\n')
        continue

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if not has_uppercase:
        print('Error: your password has no uppercase.\n')
    elif not has_lowercase:
        print('Error: your password has no lowercase.\n')
    elif not has_digit:
        print('Error: your password has no digit.\n')
    elif not has_special:
        print('Error: your password has no special character.\n')
    else:
        print('Your password is strong.')
        break