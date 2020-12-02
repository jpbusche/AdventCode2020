""" Code for Day 1, Puzzle 2 in Advent Code 2020 """

with open('input1.txt') as f:
    lines = [int(line.rstrip()) for line in f]

found = False
for i, value in enumerate(lines):
    for j, value2 in enumerate(lines[i + 1:]):
        for value3 in lines[j + 1:]:
            if value + value2 + value3 == 2020:
                found = True
                break
        if found: break
    if found: break

print(value * value2 * value3)