def solve():
    with open('../input.txt', 'r') as f:
        rotations = f.read().strip().split('\n')
    
    position = 50
    count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:  # direction == 'R'
            position = (position + distance) % 100
        
        if position == 0:
            count += 1
    
    return count

if __name__ == '__main__':
    result = solve()
    print(result)

