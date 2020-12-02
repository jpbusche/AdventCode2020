""" Code for Day 1, Puzzle 1 in Advent Code 2020 """

with open('input1.txt') as f:
    lines = [int(line.rstrip()) for line in f]

i, j = 0, len(lines) - 1
lines.sort()
while True:
    a, b = lines[i], lines[j]
    if a + b == 2020: break
    elif a + b > 2020: j -= 1
    else: i += 1

print(a * b)