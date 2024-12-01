#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream inputFile("../input.txt");

    std::string instructions;
    std::getline(inputFile, instructions);
    inputFile.close();

    int floor = 0;

    int position = 0;
    for (char c : instructions) {
        ++position;
        if (c == '(') {
            ++floor;  
        } else if (c == ')') {
            --floor;  
        }

        std::cout << "Santa is on floor: " << floor << std::endl;
        
        if (floor == -1) {
            std::cout << "Santa enters the basement at position: " << position << std::endl;
            break;
        }
    }

    std::cout << "Santa ends up on floor: " << floor << std::endl;

    return 0;
}
