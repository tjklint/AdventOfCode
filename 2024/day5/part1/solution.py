import os
from collections import defaultdict

with open('../input.txt', 'r') as file:
    lines = file.read().strip().split("\n")

rules = []
updates = []
is_rule_section = True

for line in lines:
    if line.strip() == "":
        is_rule_section = False
    elif is_rule_section:
        rules.append(tuple(map(int, line.split("|"))))
    else:
        updates.append(list(map(int, line.split(","))))

def build_graph(rules):
    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)
    return graph

def is_valid_update(update, graph):
    index_map = {page: i for i, page in enumerate(update)}
    for x in graph:
        for y in graph[x]:
            if x in index_map and y in index_map:
                if index_map[x] > index_map[y]:  
                    return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

graph = build_graph(rules)
total_middle_sum = 0

for update in updates:
    if is_valid_update(update, graph):
        total_middle_sum += find_middle_page(update)

print("Sum of middle pages:", total_middle_sum)
