#include <iostream>
#include <string>
#include <cctype>

using namespace std;

// Function to validate the Left-Hand Side (LHS) of a production rule
bool isValidLHS(const string& lhs) {
    // Check if the LHS is a single uppercase letter
    return lhs.length() == 1 && isupper(lhs[0]);
}

int main() {
    string input;

    // Ask user for input in the form of a production rule (e.g., A -> abc)
    cout << "Enter a production rule (e.g., A -> abc): ";
    getline(cin, input);

    // Extract the LHS by finding the position of "->"
    size_t arrowPos = input.find("->");
    if (arrowPos == string::npos) {
        cout << "Invalid format. The rule should contain '->'" << endl;
        return 1;
    }

    // Get the LHS from the input (before "->")
    string lhs = input.substr(0, arrowPos);

    // Validate the LHS
    if (isValidLHS(lhs)) {
        cout << "Valid Left-Hand Side (LHS): " << lhs << endl;
    } else {
        cout << "Invalid Left-Hand Side (LHS). It should be a single uppercase letter." << endl;
    }

    return 0;
}
