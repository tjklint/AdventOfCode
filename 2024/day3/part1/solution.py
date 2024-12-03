import os
from typing import List
import re

def main(): 
    with open('../input.txt', 'r') as file:
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, file.read())

        total_sum = sum(int(x) * int(y) for x, y in matches)
        print(f"Total sum: {total_sum}")


if __name__ == '__main__':
    main()