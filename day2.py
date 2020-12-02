f = open("day2Input.txt")
lines = f.readlines()
cleanLines = [line.strip() for line in lines]
valid = 0
for item in cleanLines:
	subject = item.split()
	valid_range = subject[0].split("-")
	low = int(valid_range[0])
	up = int(valid_range[1])
	letter = subject[1].split(":")[0]
	password = subject[2]

	low_true = password[low - 1] == letter
	up_true = password[up - 1] == letter
	if (not low_true and up_true) or (not up_true and low_true):
		valid += 1	
print valid
	# for password_letter in password:
	# 	if letter == password_letter:
	# 		count +=1
	# if count >= low and count <= up:
	# 	valid +=1
