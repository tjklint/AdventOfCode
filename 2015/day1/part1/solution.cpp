#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream inputFile("../input.txt");

    std::string instructions;
    std::getline(inputFile, instructions);
    inputFile.close();

    int floor = 0;

    for (char c : instructions) {
        if (c == '(') {
            ++floor;  
        } else if (c == ')') {
            --floor;  
        }
    }

    std::cout << "Santa ends up on floor: " << floor << std::endl;

    return 0;
}
