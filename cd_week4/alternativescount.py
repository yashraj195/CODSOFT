# Function to validate the Left-Hand Side (LHS) of the production rule
def is_valid_lhs(lhs):
    # Check if the LHS is a single uppercase letter (non-terminal)
    return len(lhs) == 1 and lhs.isupper()

# Function to validate the Right-Hand Side (RHS) with alternatives
def is_valid_rhs(rhs):
    # Split RHS by '/' for alternatives
    alternatives = rhs.split('/')
    
    # Check if each alternative is either lowercase letters or epsilon (ε)
    for alternative in alternatives:
        if alternative != 'ε' and not alternative.islower():
            return False
    return True

# Function to count the number of alternatives in the RHS
def count_alternatives(rhs):
    # Split RHS by '/' for alternatives and count the length
    alternatives = rhs.split('/')
    return len(alternatives)

# Function to validate the entire production rule and count alternatives
def is_valid_production_rule(rule):
    # Check if the rule contains "->"
    if "->" not in rule:
        return False
    
    # Split the rule into LHS and RHS
    lhs, rhs = rule.split("->", 1)  # Split only at the first "->"
    
    # Validate LHS and RHS
    if not is_valid_lhs(lhs) or not is_valid_rhs(rhs):
        return False
    
    # Count the number of alternatives in RHS
    num_alternatives = count_alternatives(rhs)
    print(f"Number of alternatives in RHS: {num_alternatives}")
    
    return True

def main():
    # Ask user for input in the form of a production rule (e.g., A -> abc or A -> ε)
    input_rule = input("Enter a production rule (e.g., A -> abc or A -> ε): ")
    
    # Validate the input production rule
    if is_valid_production_rule(input_rule):
        print("Valid production rule!")
    else:
        print("Invalid production rule!")

if __name__ == "__main__":
    main()
