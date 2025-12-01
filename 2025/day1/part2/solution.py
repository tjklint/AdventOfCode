def solve():
    with open('../input.txt', 'r') as f:
        rotations = f.read().strip().split('\n')
    
    position = 50
    count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
    
        if direction == 'L':
            for k in range(1, distance + 1):
                if (position - k) % 100 == 0:
                    count += 1
            position = (position - distance) % 100
        else:  # direction == 'R'
            for k in range(1, distance + 1):
                if (position + k) % 100 == 0:
                    count += 1
            position = (position + distance) % 100
    
    return count

if __name__ == '__main__':
    result = solve()
    print(result)

