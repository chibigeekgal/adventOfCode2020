import copy

f = open("day11Input.txt")
lines = f.readlines()
cleanLines = [list(line.strip("\n")) for line in lines]

def occupied_number(array, i, j):
	number = 0
	if i > 0:
		if j > 0:
			if array[i - 1][j - 1] == '#':
				number += 1
		if array[i - 1][j] == '#':
			number += 1
		if j < (len(cleanLines[i]) - 1):
			if array[i - 1][j + 1] == '#':
				number += 1
	if j > 0:
		if array[i][j - 1] == '#':
			number += 1
	if j < (len(cleanLines[i]) - 1):
		if array[i][j + 1] == '#':
			number += 1
	if i < (len(cleanLines) - 1):
		if j > 0:
			if array[i + 1][j - 1] == '#':
				number += 1
		if j < (len(cleanLines[i]) - 1):
			if array[i + 1][j + 1] == '#':
				number += 1
		if array[i + 1][j] == '#':
			number += 1
	return number

def occupied_number_v2(array, i, j):
	number = 0
	#left up
	for x in reversed(range(0, i)):
		diff = i - x
		y = j - diff
		if y >= 0:
			if array[x][y] == '#':
				number += 1
				break
			if array[x][y] == 'L':
				break
		else:
			break
	#middle up
	for x in reversed(range(0, i)):
		diff = i - x
		y = j
		if array[x][y] == '#':
			number += 1
			break
		if array[x][y] == 'L':
			break
	#right up
	for x in reversed(range(0, i)):
		diff = i - x
		y = j + diff
		if y < len(cleanLines[i]):
			if array[x][y] == '#':
				number += 1
				break
			if array[x][y] == 'L':
				break
		else:
			break
	#left down
	for x in range(i + 1, len(cleanLines)):
		diff = x - i
		y = j - diff
		if y >= 0:
			if array[x][y] == '#':
				number += 1
				break
			if array[x][y] == 'L':
				break
		else:
			break
	#middle down
	for x in range(i + 1, len(cleanLines)):
		diff = x - i
		y = j
		if array[x][y] == '#':
			number += 1
			break
		if array[x][y] == 'L':
			break
	#right down
	for x in range(i + 1, len(cleanLines)):
		diff = x - i
		y = j + diff
		if y < len(cleanLines[x]):
			if array[x][y] == '#':
				number += 1
				break
			if array[x][y] == 'L':
				break
		else:
			break
	#middle left
	for y in reversed(range(0, j)):
		x = i
		if array[x][y] == '#':
			number += 1
			break
		if array[x][y] == 'L':
			break
	#middle right
	for y in range(j + 1, len(cleanLines[i])):
		x = i
		if array[x][y] == '#':
			number += 1
			break
		if array[x][y] == 'L':
			break
	return number
	
cleanLinesCopy = copy.deepcopy(cleanLines)
while True:
	for i in range(0, len(cleanLines)):
		for j in range(0, len(cleanLines[i])):
			if cleanLines[i][j] == 'L':
				if occupied_number_v2(cleanLines, i, j) == 0:
					cleanLinesCopy[i][j] = '#'
			elif cleanLines[i][j] == '#':
				if occupied_number_v2(cleanLines, i, j) >= 5:
					cleanLinesCopy[i][j] = 'L'
	if cleanLinesCopy == cleanLines:
		break
	else:
		cleanLines = copy.deepcopy(cleanLinesCopy)


number = 0
for i in range(0, len(cleanLinesCopy)):
	for j in range(0, len(cleanLinesCopy[i])):
		if cleanLinesCopy[i][j] == '#':
			number += 1

print number