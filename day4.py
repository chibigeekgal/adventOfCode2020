def valid_input(input_dict):
	for (key, value) in input_dict.items():
		if key == 'byr':
			year = int(value)
			if year < 1920 or year > 2002:
				return False
		if key == 'iyr':
			year = int(value)
			if year < 2010 or year > 2020:
				return False
		if key == 'eyr':
			year = int(value)
			if year < 2020 or year > 2030:
				return False
		if key == 'hgt':
			unit = value[-2:]  
			try:
				if unit == 'cm':
					if len(value) != 5:
						return False
					number = int(value[:3])
					if number < 150 or number > 193:
						return False
				elif unit == 'in':
					if len(value) != 4:
						return False
				 	number = int(value[:2])
					if number < 59 or number > 76:
						return False
				else:
					return False
			except ValueError:
				return False
		if key == 'hcl':
			valid_input = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
			if value[0] != '#' or len(value) != 7:
				return False
			for digit in value[-6:]:
				if not digit in valid_input:
					return False
		if key == 'ecl':
			valid_input = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
			if not value in valid_input:
				return False
		if key == 'pid':
			if len(value) != 9:
				return False
			try:
				int_value = int(value)
			except ValueError:
				return False	
	return True

f = open("day4Input.txt")
lines = f.readlines()

valid = 0
valid_items = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
input_dict = {}
for line in lines:
	if line == '\n':
		if set(input_dict.keys()).issuperset(valid_items):
			if valid_input(input_dict):
				#print input_dict
				valid += 1	
			else:
				print input_dict		
		input_dict_keys = {}
	items = line.split(" ")
	for item in items:
		split = item.split(":")
		if len(split) != 2:
			continue
		key = split[0]
		input_dict[key] = split[1].rstrip()


print valid
