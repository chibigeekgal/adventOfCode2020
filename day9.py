def is_sub_sum(subarray, number):
	for n1 in range(0, len(subarray)):
		for n2 in range(0, len(subarray)):
			if n1 != n2:
				if (subarray[n1] + subarray[n2]) == number:
					return True
	return False


f = open("day9Input.txt")
lines = f.readlines()
cleanLines = [int(line.strip("\n")) for line in lines]

preamble = 25

for i in range(preamble, len(cleanLines)):
	subarray = cleanLines[i-preamble:i]
	if not is_sub_sum(subarray, cleanLines[i]):
		print cleanLines[i]



number = 1124361034
for i in range(0, len(cleanLines)):
	for j in range(0, len(cleanLines)):
		subarray = cleanLines[i:j]
		if sum(subarray) == number:
			print min(subarray), max(subarray), min(subarray) + max(subarray)