from app import leetlist
idx = 0

password = input("input your best password> ")
# Mangle jtr word list
f = open('john.txt', 'r')
words = f.readlines()
for word in words:
	leets = leetlist(word)
	length = len(leets)
	for perm in leets:
		if ''.join(perm) == password:
			print("found")
			exit()
		idx += 1
		if idx % 1000000 == 0:
			print(''.join(perm), " of ", length)
f.close()