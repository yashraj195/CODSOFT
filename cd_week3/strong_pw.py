import re

def is_strong_password(password):
    # Check the length of the password
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character (!@#$%^&*(), etc.)."
    
    # If all conditions are met
    return "Password is strong."

# Input password
password = input("Enter your password: ")

# Check the strength of the password
result = is_strong_password(password)
print(result)