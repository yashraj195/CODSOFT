# Function to validate the Left-Hand Side (LHS) of the production rule
def is_valid_lhs(lhs):
    # Check if the LHS is a single uppercase letter (non-terminal)
    return len(lhs) == 1 and lhs.isupper()

def main():
    # Ask user for input in the form of a production rule (e.g., A -> abc)
    input_rule = input("Enter a production rule (e.g., A -> abc): ")
    
    # Split the input rule at "->"
    if "->" not in input_rule:
        print("Invalid production rule!")
        return

    lhs = input_rule.split("->")[0]  # Left-hand side (before "->")
    
    # Validate the LHS
    if is_valid_lhs(lhs):
        print("Valid Left-Hand Side!")
    else:
        print("Invalid Left-Hand Side!")

if __name__ == "__main__":
    main()
