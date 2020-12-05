import math
f = open("day5Input.txt")
lines = f.readlines()
cleanLines = [line.strip() for line in lines]

def seat_id(line):
	lower_row = 0
 	upper_row = 127
 	for i in range(0, 7):
		if line[i] == 'F':
			upper_row = upper_row - math.ceil(float(upper_row - lower_row)/2)
		if line[i] == 'B':
			lower_row = lower_row + math.ceil(float(upper_row - lower_row)/2)
	lower_column = 0
	upper_column = 7
	for i in range(7, 10):
		if line[i] == 'L':
			upper_column = upper_column - math.ceil(float(upper_column - lower_column)/2)
		if line[i] == 'R':
			lower_column = lower_column + math.ceil(float(upper_column - lower_column)/2)
	seat_id = lower_row * 8 + lower_column
	return seat_id

	
print set(range(1, 951)) - set(sorted(map(seat_id, cleanLines)))
