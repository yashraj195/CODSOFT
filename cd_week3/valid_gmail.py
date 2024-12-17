import re

def is_valid_gmail(email):
    return bool(re.match(r'^[a-z0-9._]+@gmail\.com$', email)) and "Valid Gmail ID" or "Invalid Gmail ID"

# Example usage
email = input("Enter your Gmail ID: ")
print(is_valid_gmail(email))