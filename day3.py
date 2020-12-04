from functools import reduce

f = open("day3Input.txt")
lines = f.readlines()
cleanLines = [line.strip() for line in lines]

moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

all_trees = []
for (right, down) in moves:
	column = 0
	row = 0
	trees = 0
	while row < len(cleanLines):
		if cleanLines[row][column % len(cleanLines[row])] == '#':
			trees += 1
		column += right
		row += down

	all_trees.append(trees)

print reduce(lambda x, y: x*y, all_trees)