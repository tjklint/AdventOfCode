def is_invalid_id(id_num):
    id_str = str(id_num)
    n = len(id_str)
    
    for k in range(2, n + 1):
        if n % k != 0:
            continue
        
        part_length = n // k
        first_part = id_str[:part_length]
        
        all_same = True
        for i in range(1, k):
            part = id_str[i * part_length:(i + 1) * part_length]
            if part != first_part:
                all_same = False
                break
        
        if all_same:
            return True
    
    return False

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

