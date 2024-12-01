import os 
from typing import List

def main():
    list1: List[int] = []
    list2: List[int] = []
    total: int = 0

    with open('../input.txt', 'r') as file:
        for line in file:
            list1.append(int(line.strip().split("   ")[0]))
            list2.append(int(line.strip().split("   ")[1]))

    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])

    print(f"Total: {total}")

if __name__ == '__main__':
    main()