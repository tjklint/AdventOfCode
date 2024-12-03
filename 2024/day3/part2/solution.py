import os
from typing import List
import re

def main(): 
    with open('../input.txt', 'r') as file:
        mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"  # Matches valid mul instructions
        do_pattern = r"do\(\)"                       # Matches do() instructions
        dont_pattern = r"don't\(\)"                  # Matches don't() instructions

        mul_enabled = True  
        total_sum = 0

        matches = re.finditer(rf"{mul_pattern}|{do_pattern}|{dont_pattern}", file.read())

        for match in matches:
            match = match.group()
            
            if match == "do()":
                mul_enabled = True
            elif match == "don't()":
                mul_enabled = False
            else:
                if mul_enabled:
                    x, y = map(int, re.match(mul_pattern, match).groups())
                    total_sum += x * y

    print(f"Total sum: {total_sum}")

if __name__ == '__main__':
    main()