#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

int countGroupAnswersAny(const std::string& group) {
	std::unordered_set<char> answers;
	for (char c : group) {
		if (c >= 'a' && c <= 'z') {
			answers.insert(c);
		}
	}
	return answers.size();
}

int countGroupAnswersAll(const std::string& group, int groupSize) {
	std::vector<int> count(26, 0);
	for (char c : group) {
		if (c >= 'a' && c <= 'z') {
			count[c - 'a']++;
		}
	}

	return std::count_if(count.begin(), count.end(), [groupSize](int c) { return c == groupSize; });
}

int main() {
	std::ifstream file("day6input.txt");

	std::string line;
	std::string group;
	int totalAny = 0;
	int totalAll = 0;
	int groupSize = 0;

	while (std::getline(file, line)) {
		if (line.empty()) {
			totalAny += countGroupAnswersAny(group);
			totalAll += countGroupAnswersAll(group, groupSize);
			group.clear();
			groupSize = 0;
		}
		else {
			group += line;
			groupSize++;
		}
	}

	if (!group.empty()) {
		totalAny += countGroupAnswersAny(group);
		totalAll += countGroupAnswersAll(group, groupSize);
	}

	std::cout << "Part 1 answer: " << totalAny << std::endl;
	std::cout << "Part 2 answer: " << totalAll << std::endl;

	return 0;
}