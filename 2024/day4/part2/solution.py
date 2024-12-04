file_path = "../input.txt"

with open(file_path, 'r') as f:
    grid = [list(line.strip()) for line in f.readlines()]

def find_all_x_mas(word_search):
    x_mas_amount = 0
    for x in range(1, len(word_search) - 1):  # Avoid edges
        for y in range(1, len(word_search[0]) - 1):  # Avoid edges
            if word_search[x][y] == "A" \
            and {word_search[x - 1][y - 1], word_search[x + 1][y + 1]} == {"M", "S"} \
            and {word_search[x + 1][y - 1], word_search[x - 1][y + 1]} == {"M", "S"}:
                x_mas_amount += 1
    return x_mas_amount

print(find_all_x_mas(grid))  
