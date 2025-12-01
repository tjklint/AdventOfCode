# Test with the example from the problem
rotations = [
    "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"
]

position = 50
count = 0

for i, rotation in enumerate(rotations):
    direction = rotation[0]
    distance = int(rotation[1:])
    
    print(f"Rotation {i+1}: {rotation}, starting at {position}")
    
    zero_count = 0
    if direction == 'L':
        for k in range(1, distance + 1):
            if (position - k) % 100 == 0:
                zero_count += 1
                print(f"  Passed through 0 at k={k}")
        position = (position - distance) % 100
    else:  # direction == 'R'
        for k in range(1, distance + 1):
            if (position + k) % 100 == 0:
                zero_count += 1
                print(f"  Passed through 0 at k={k}")
        position = (position + distance) % 100
    
    count += zero_count
    print(f"  Zero count for this rotation: {zero_count}, new position: {position}, total count: {count}")

print(f"\nTotal count: {count} (expected: 6)")

