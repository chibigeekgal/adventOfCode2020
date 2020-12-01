f = open("day1Input.txt")
lines = f.readlines()
cleanLines = [int(line.strip()) for line in lines]

print len(cleanLines)

for a in cleanLines:
	for b in cleanLines:
		for c in cleanLines:

			if (a + b + c) == 2020:
				print a * b * c
