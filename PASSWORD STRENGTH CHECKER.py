import string

def check_password_strength(password):
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length < 6:
        return "❌ Weak Password (Too Short)"
    elif score == 4 and length >= 8:
        return "✅ Strong Password"
    elif score >= 2:
        return "⚠️ Medium Password"
    else:
        return "❌ Weak Password"


if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = check_password_strength(pwd)
    print("Password Strength:", result)