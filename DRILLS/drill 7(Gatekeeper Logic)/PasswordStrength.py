# Implement password_strength(password). Return Weak if the password has
# fewer than 8 characters. Return Medium if it has at least 8 characters
# but does not contain both letters and digits. Return Strong if it has at
# least 8 characters and contains at least one letter and at least one digit. 
# Students may need to research isalpha and isdigit.

def password_strength(password):
    length = len(password)

    if length < 8:
        return "Weak"

    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_letter and has_digit:
        return "Strong"
    else:
        return "Medium"