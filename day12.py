import numpy as np
import math

f = open("day12Input.txt")
lines = f.readlines()
cleanLines = [line.strip("\n") for line in lines]

# E S W N
distances = [0, 0, 0, 0]
way_point = [10, 0, 0, 1]
curr_index = 0

for line in cleanLines:
	dist = int(line[1:])
	if line[0] == 'N':
		oppo_dist = way_point[1]
		if oppo_dist > dist:
			way_point[1] = oppo_dist - dist
		else:
			way_point[1] = 0
			way_point[3] += dist - oppo_dist
		print "north ", dist, oppo_dist
	if line[0] == 'S':
		oppo_dist = way_point[3]
		if oppo_dist > dist:
			way_point[3] = oppo_dist - dist
		else:
			way_point[3] = 0
			way_point[1] += dist - oppo_dist
		print "south ", dist, oppo_dist, way_point
	if line[0] == 'E':
		oppo_dist = way_point[2]
		if oppo_dist > dist:
			way_point[2] = oppo_dist - dist
		else:
			way_point[2] = 0
			way_point[0] += dist - oppo_dist
		print "east ", dist, oppo_dist, way_point
	if line[0] == 'W':
		oppo_dist = way_point[0]
		if oppo_dist > dist:
			way_point[0] = oppo_dist - dist
		else:
			way_point[0] = 0
			way_point[2] += dist - oppo_dist
		print "west ", dist, oppo_dist, way_point
	if line[0] == 'L':
		curr_index = (curr_index - (int(line[1:])/90)) % 4
	if line[0] == 'R':
		curr_index = (curr_index + (int(line[1:])/90)) % 4
	if line[0] == 'F':
		mag = int(line[1:])
		if curr_index == 0:
			point = way_point
		else:
			point = way_point[-curr_index:]
			point = point + way_point[:4 - curr_index]
		print "point ", point
		move = map(lambda x: x * mag, point)
		indexes = []
		for i in range(0 ,4):
			if move[i] != 0:
				indexes.append(i)
		print "move prev ", move
		for i in indexes:
			oppo_dist = distances[(i + 2) % 4]
			if oppo_dist > move[i]:
				distances[(i + 2)%4] = oppo_dist - move[i]
			else:
				distances[(i + 2)%4] = 0
				distances[i] += move[i] - oppo_dist
		print "move after ", move
	print line
	print curr_index
	print way_point
	print "distances ", distances

print distances
