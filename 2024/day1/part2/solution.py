import os 
from typing import List

def main():
    with open('../input.txt', 'r') as file:
        data = [line.strip().split("   ") for line in file]

    list1: List[int] = [int(entry[0]) for entry in data]
    list2: List[int] = [int(entry[1]) for entry in data]

    count_map = {}
    for num in list2:
        count_map[num] = count_map.get(num, 0) + 1

    total: int = 0
    for num in list1:
        count = count_map.get(num, 0)
        total += num * count
    
    print(f"Total: {total}")
    
if __name__ == '__main__':
    main()