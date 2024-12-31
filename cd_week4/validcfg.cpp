#include <iostream>
#include <sstream>
#include <string>
#include <cctype>

using namespace std;

// Function to validate the production rule
bool isValidProductionRule(const string& input) {
    // Find the position of "->"
    size_t arrowPos = input.find("->");
    
    if (arrowPos == string::npos) {
        // If "->" is not found, it's an invalid rule
        return false;
    }
    
    // Extract left-hand side (non-terminal) and right-hand side (terminals)
    string lhs = input.substr(0, arrowPos);
    string rhs = input.substr(arrowPos + 2); // Skip the "->"

    // Check if LHS is a single uppercase letter (non-terminal)
    if (lhs.length() != 1 || !isupper(lhs[0])) {
        return false;
    }

    // Check if RHS contains only lowercase letters (terminals)
    for (char ch : rhs) {
        if (!islower(ch)) {
            return false; // If any character is not a lowercase letter, it's invalid
        }
    }

    return true;
}

int main() {
    string input;
    
    // Ask user for input in the form of a production rule (e.g., A -> abc)
    cout << "Enter a production rule (e.g., A -> abc): ";
    getline(cin, input);

    // Validate the input
    if (isValidProductionRule(input)) {
        cout << "Valid production rule!" << endl;
    } else {
        cout << "Invalid production rule!" << endl;
    }

    return 0;
}
