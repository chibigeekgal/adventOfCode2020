import copy

f = open("day8Input.txt")
lines = f.readlines()
originalLines = [line.strip("\n") for line in lines]

triedIndex = 0
while triedIndex < len(originalLines):
	cleanLines = copy.copy(originalLines)
	if "nop" in cleanLines[triedIndex]:
		cleanLines[triedIndex] = "jmp" + cleanLines[triedIndex][3:]
	elif "jmp" in cleanLines[triedIndex]:
		cleanLines[triedIndex] = "nop" + cleanLines[triedIndex][3:]
	accum = 0
	index = 0
	visited = [False for i in range(0, len(cleanLines))]
	while True:
		if index >= len(cleanLines):
			break
		if visited[index]: 
			break
		visited[index] = True
		instruct = cleanLines[index].split(" ")
		if instruct[0] == "acc":
			amount = int(instruct[1])
			accum += amount
			index += 1
		if instruct[0] == "jmp":
			index += int(instruct[1])
		if instruct[0] == "nop":
			index += 1
	if index == len(cleanLines):
		print accum
		break
	else:
		triedIndex += 1