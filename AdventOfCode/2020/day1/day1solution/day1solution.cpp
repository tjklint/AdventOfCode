// Day 1, Part 1 + 2 for Advent Of Code 2022.
// Begrudgingly learning C++ with it.

#include <iostream>
#include <fstream>
#include <vector>

int main()
{
    // Initialize input.
    std::ifstream inputFile("day1input.txt");
    std::vector<int> expenses;
    int expense;
    // Read the expense report from the file
    while (inputFile >> expense) {
        expenses.push_back(expense);
    }

    // C++ makes my brain hurt.
    for (size_t i = 0; i < expenses.size(); ++i) {
        for (size_t j = i + 1; j < expenses.size(); ++j) {
            if (expenses[i] + expenses[j] == 2020) {
                int twoResultMultiplied = expenses[i] * expenses[j];
                std::cout << "The sum of the two numbers adding up to 2020 are " <<
                    expenses[i] << " and " << expenses[j] << ". They multiply to: " << twoResultMultiplied << std::endl;
            }
        }
    }

    // My headache might hospitalize me.
    for (size_t i = 0; i < expenses.size(); ++i) {
        for (size_t j = i + 1; j < expenses.size(); ++j) {
            for (size_t k = j + 1; k < expenses.size(); ++k) {
                if (expenses[i] + expenses[j] + expenses[k] == 2020) {
                    // Multiply the three numbers and print the result
                    int threeResultMultiplied = expenses[i] * expenses[j] * expenses[k];
                    std::cout << "The three numbers that add up to 2020 are " << expenses[i] << ", " << expenses[j] << ", and " <<
                        expenses[k] << ". They multiply to: " << threeResultMultiplied << std::endl;
                    return 0;
                }
            }
        }
    }
}
