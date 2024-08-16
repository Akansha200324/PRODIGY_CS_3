import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[@$!%*?&#]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., @$!%*?&#).")

    # Strength assessment
    if strength == 5:
        return "Strong password!", feedback
    elif 3 <= strength < 5:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")

    strength, feedback = assess_password_strength(password)
    print(f"Password strength: {strength}")

    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
