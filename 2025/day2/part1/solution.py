def is_invalid_id(id_num):
    id_str = str(id_num)
    n = len(id_str)
    
    if n % 2 != 0:
        return False
    
    half = n // 2
    first_half = id_str[:half]
    second_half = id_str[half:]
    
    return first_half == second_half

def solve():
    with open('../input.txt', 'r') as f:
        line = f.read().strip()
    
    ranges = []
    for range_str in line.split(','):
        if not range_str:
            continue
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    
    invalid_ids = []
    
    for start, end in ranges:
        for id_num in range(start, end + 1):
            if is_invalid_id(id_num):
                invalid_ids.append(id_num)
    
    return sum(invalid_ids)

if __name__ == '__main__':
    result = solve()
    print(result)

