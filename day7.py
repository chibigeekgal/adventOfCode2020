import math
f = open("day7Input.txt")
lines = f.readlines()
cleanLines = [line.strip("\n") for line in lines]

can_be_contained = {}
contains = {}

for line in cleanLines:
	split = line.split("s contain")
	left = " ".join(split[0].split(" ")[:-1])
	rights = split[1].split(",")
	for right in rights:
		if "no other bag" in right:
			continue
		number = int(right.split(" ")[1])
		bag = " ".join(right.split(" ")[2:-1])
		if left in can_be_contained:
			for i in range(0, number):
				can_be_contained[left].append(bag)
		else:
			can_be_contained[left] = [bag for i in range(0, number)]


print can_be_contained

bag_sets = []
queue = ["shiny gold"]

while len(queue) > 0:
	curr_bag = queue.pop(0)
	if curr_bag in can_be_contained:
		for bag in can_be_contained[curr_bag]:
				bag_sets.append(bag)
				queue.append(bag)

print bag_sets
print len(bag_sets)