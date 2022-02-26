import os
from pprint import pprint as pp

input = open(os.getcwd() + r"\data\rosalind_fibd.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read().split(' ')
months = int(data[0])
lifespan = int(data[1])

print(months, lifespan)
rabbits = [1]
for l in range(1, lifespan):
	rabbits += [0]

label = 'm   '
for i in range(lifespan):
	label += '|{0:3} '.format(i)
print(label)

first_month = '  1  1  '
for i in range(1, lifespan):
	first_month += '  0  '
print(first_month)

for m in range(2, months+1):

	# find number of adults this month
	adults = 0
	for i in range(1, lifespan):
		adults += rabbits[i]
	
	# adults all have kids
	child = adults

	# everyone gets a birthday
	for i in range(lifespan-1, 0, -1):
		rabbits[i] = rabbits[i-1]
	rabbits[0] = child

	# print month
	label = '{0:3} '.format(m)
	for i in range(lifespan):
		label += ' {!s:<3.3} '.format(rabbits[i])
	print(label)
	
total = 0
for r in rabbits:
	total += r

print(total)
output.write(str(total))

input.close()
output.close()