import os
from typing import List

def main(): 
    safe_total = 0

    with open('../input.txt', 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe(report) or can_be_safe_with_removal(report):
                safe_total += 1

    print(f"Safe total with problem dampener: {safe_total}")
    

def is_safe(report: List[int]) -> bool:
    is_increasing = True
    for i in range(len(report) - 1):
        if report[i] >= report[i + 1]:
            is_increasing = False
            break

    is_decreasing = True
    for i in range(len(report) - 1):
        if report[i] <= report[i + 1]:
            is_decreasing = False
            break

    valid_differences = True
    for i in range(len(report) - 1):
        difference = abs(report[i] - report[i + 1])
        if difference < 1 or difference > 3:
            valid_differences = False
            break

    return (is_increasing or is_decreasing) and valid_differences


def can_be_safe_with_removal(report: List[int]) -> bool:
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:] 
        if is_safe(modified_report):
            return True
    return False


if __name__ == '__main__':
    main()