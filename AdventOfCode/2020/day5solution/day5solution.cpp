#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

int decode(const std::string& inputString, char lower, char upper) {
    int min = 0; // Init
    int max = (1 << inputString.size()) - 1; // Init upper bound from the length of the string

    // Iterate through each char
    for (char c : inputString) {
        int mid = (min + max) / 2; // Find the middle value

        if (c == lower) { // Checks the lower.
            max = mid;
        }
        else if (c == upper) { // Checks the upper.
            min = mid + 1;
        }
    }

    return min;
}

int main() {
    // Open the input file for reading
    std::ifstream file("day5input.txt");
    std::string line;

    int highestSeatId = 0; // To store the highest seat ID
    std::vector<int> seatIds; // Vector to store all seat IDs for Part 2

    // Read file line by line
    while (std::getline(file, line)) {
        // Decode the first 7 chars for row
        int row = decode(line.substr(0, 7), 'F', 'B');
        // Decode the next 3 chars for column
        int col = decode(line.substr(7, 3), 'L', 'R');

        // Calc the seat ID
        int seatId = row * 8 + col;

        // Add seat ID to the vector
        seatIds.push_back(seatId);

        // Update the highest seat ID for Part 1
        highestSeatId = std::max(highestSeatId, seatId);
    }

    std::cout << "The highest seat ID is: " << highestSeatId << std::endl;

    // Part 2
    // Sort the seat IDs
    std::sort(seatIds.begin(), seatIds.end());

    // Check to find the missing seat ID
    for (size_t i = 1; i < seatIds.size(); ++i) {
        if (seatIds[i] - seatIds[i - 1] == 2) { // Check if there's a gap of 2 between adjacent seat IDs
            std::cout << "Your seat ID is: " << (seatIds[i] - 1) << std::endl; // Seat ID is in the gap
            break;
        }
    }

    return 0;
}