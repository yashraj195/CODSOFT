import re

# Function to validate the Left-Hand Side (LHS) of a production rule
def is_valid_lhs(lhs):
    # Check if the LHS is a single uppercase letter
    return len(lhs) == 1 and lhs.isupper()

# Function to validate the Right-Hand Side (RHS) with multiple alternatives
def is_valid_rhs(rhs):
    # Split RHS by '/' symbol for alternatives
    alternatives = rhs.split('/')
    
    # Validate each alternative
    for alternative in alternatives:
        if not alternative.islower():  # RHS alternatives must be all lowercase
            return False
    return True

# Function to validate a single production rule
def is_valid_production_rule(rule):
    # Check if the rule contains "->"
    if "->" not in rule:
        return False
    
    # Split the rule into LHS and RHS
    lhs, rhs = rule.split("->", 1)  # Split only at the first "->"
    
    # Validate LHS and RHS
    return is_valid_lhs(lhs) and is_valid_rhs(rhs)

# Main function to read multiple production rules and count valid ones
def main():
    num_valid_rules = 0
    
    print("Enter multiple production rules (one per line). Type 'end' to stop input.")
    
    while True:
        # Read each production rule from the user
        rule = input().strip()
        
        if rule.lower() == 'end':  # Stop when user types "end"
            break
        
        # Validate the production rule
        if is_valid_production_rule(rule):
            num_valid_rules += 1
    
    # Output the total number of valid production rules
    print(f"Total number of valid production rules: {num_valid_rules}")

# Run the main function
if __name__ == "__main__":
    main()
