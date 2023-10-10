#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

// Function to check if a password is valid according to the rules
bool isValidPassword(const std::string& rules, const std::string& password) {
	// istringstream makes an instance of std::istringstream, contains the rules string.
	// allows it to be read as an input stream.
	std::istringstream istringstream(rules);
	int minCount, maxCount;
	char requiredChar, dash;
	istringstream >> minCount >> dash >> maxCount >> requiredChar;

	int charCount = 0;
	for (char c : password) {
		if (c == requiredChar) {
			charCount++;
		}
	}

	return charCount >= minCount && charCount <= maxCount;
}

// Part 2 Password Checker, checks if a password is valid according to the new rules.
bool newIsPasswordValid(int pos1, int pos2, char letter, const std::string& password) {
	// Check if exactly one of the positions contains the required letter.
	return (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter);
}

int main() {

    // Open the file.
    std::ifstream input("day2input.txt"); 

    int validCount = 0; // Count of valid passwords for Part 1.
    int newValidCount = 0; // Count of valid passwords for Part 2.
    std::string line;

    while (std::getline(input, line)) {
        size_t colonPos = line.find(':');
        std::string policy = line.substr(0, colonPos); // Rules before the colon
        std::string password = line.substr(colonPos + 2); // Password after the colon and space

        // Parse the minCount, maxCount, and requiredChar
        std::stringstream ss(policy);
        int pos1, pos2;
        char reqChar, dash;
        ss >> pos1 >> dash >> pos2 >> reqChar;

        // Check if the password is valid according to Part 1 and update the count.
        if (isValidPassword(policy, password)) {
            validCount++;
        }

        // Check if the password is valid according Part 2 and update the count.
        if (newIsPasswordValid(pos1, pos2, reqChar, password)) {
            newValidCount++;
        }
    }

    // Print the number of valid passwords for both sets of rules.
    std::cout << "Number of valid passwords (Part 1): " << validCount << std::endl;
    std::cout << "Number of valid passwords (Part 2): " << newValidCount << std::endl;

    return 0;
}