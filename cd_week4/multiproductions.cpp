#include <iostream>
#include <sstream>
#include <string>
#include <cctype>
#include <vector>

using namespace std;

// Function to validate the Left-Hand Side (LHS) of a production rule
bool isValidLHS(const string& lhs) {
    // Check if the LHS is a single uppercase letter
    return lhs.length() == 1 && isupper(lhs[0]);
}

// Function to validate the Right-Hand Side (RHS) with multiple alternatives
bool isValidRHS(const string& rhs) {
    stringstream ss(rhs);
    string alternative;

    // Split RHS by '/' symbol for alternatives
    while (getline(ss, alternative, '/')) {
        // Check if each alternative consists only of lowercase letters
        for (char ch : alternative) {
            if (!islower(ch)) {
                return false; // Invalid if any character is not lowercase
            }
        }
    }
    return true;
}

// Function to count the number of alternatives in the RHS
int countAlternatives(const string& rhs) {
    stringstream ss(rhs);
    string alternative;
    int count = 0;

    // Split RHS by '/' and count the alternatives
    while (getline(ss, alternative, '/')) {
        count++;
    }

    return count;
}

// Function to validate the entire production rule
bool isValidProductionRule(const string& input) {
    // Find the position of "->"
    size_t arrowPos = input.find("->");
    
    if (arrowPos == string::npos) {
        // If "->" is not found, it's an invalid rule
        return false;
    }
    
    // Extract left-hand side (LHS) and right-hand side (RHS)
    string lhs = input.substr(0, arrowPos);
    string rhs = input.substr(arrowPos + 2); // Skip the "->"

    // Validate LHS and RHS
    return isValidLHS(lhs) && isValidRHS(rhs);
}

int main() {
    string input;
    int numValidRules = 0;

    cout << "Enter multiple production rules (one per line). Type 'end' to stop input.\n";

    // Keep reading production rules until the user enters "end"
    while (true) {
        getline(cin, input);

        // Stop input when user types "end"
        if (input == "end") {
            break;
        }

        // Validate the production rule
        if (isValidProductionRule(input)) {
            numValidRules++;  // Increment the valid rule count
        }
    }

    // Output the total number of valid production rules
    cout << "Total number of valid production rules: " << numValidRules << endl;

    return 0;
}
