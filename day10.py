import math

f = open("day10Input.txt")
lines = f.readlines()
cleanLines = sorted([int(line.strip("\n")) for line in lines])


cleanLines.insert(0, 0)
cleanLines.append(max(cleanLines) + 3)
print cleanLines

ones = 1
threes = 1
lines2 = cleanLines[1:]
total = zip(cleanLines, lines2)

one_count = []
diffs = 1
curr_ones = 0
for (x, y) in total:
	if (y - x) == 1:
		one_count.append((x, y))
		curr_ones += 1
	elif (y - x) == 3:
		print curr_ones
		print one_count
		if curr_ones == 3:
			diffs *= 4
		elif curr_ones == 4:
			diffs *= 7
		elif curr_ones == 2:
			diffs *= 2
		one_count = []
		curr_ones = 0

if curr_ones == 3:
	diffs *= 4
elif curr_ones == 4:
	diffs *= 7
elif curr_ones == 2:
	diffs *= 2
print curr_ones
print one_count
print diffs
