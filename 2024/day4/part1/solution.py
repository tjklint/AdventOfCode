import os

with open('../input.txt', 'r') as f:
    grid = [line.strip() for line in f.readlines()]

word = "XMAS"
word_length = len(word)
rows = len(grid)
cols = len(grid[0])
count = 0

directions = [
    (0, 1),   # Horizontal (right)
    (1, 0),   # Vertical (down)
    (1, 1),   # Diagonal (down-right)
    (1, -1),  # Diagonal (down-left)
    (0, -1),  # Horizontal (left)
    (-1, 0),  # Vertical (up)
    (-1, -1), # Diagonal (up-left)
    (-1, 1)   # Diagonal (up-right)
]

def check_word(x, y, dx, dy):
    for i in range(word_length):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
            return False
    return True

for r in range(rows):
    for c in range(cols):
        for dx, dy in directions:
            if check_word(r, c, dx, dy):
                count += 1

print(count)