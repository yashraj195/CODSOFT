# Function to validate the production rule
def is_valid_production_rule(input_rule):
    # Find the position of "->"
    arrow_pos = input_rule.find("->")
    
    if arrow_pos == -1:
        # If "->" is not found, it's an invalid rule
        return False
    
    # Extract left-hand side (non-terminal) and right-hand side (terminals)
    lhs = input_rule[:arrow_pos]
    rhs = input_rule[arrow_pos + 2:]  # Skip the "->"

    # Check if LHS is a single uppercase letter (non-terminal)
    if len(lhs) != 1 or not lhs.isupper():
        return False

    # Check if RHS contains only lowercase letters (terminals)
    for ch in rhs:
        if not ch.islower():
            return False  # If any character is not a lowercase letter, it's invalid

    return True

def main():
    # Ask user for input in the form of a production rule (e.g., A -> abc)
    input_rule = input("Enter a production rule (e.g., A -> abc): ")

    # Validate the input
    if is_valid_production_rule(input_rule):
        print("Valid production rule!")
    else:
        print("Invalid production rule!")

if __name__ == "__main__":
    main()
