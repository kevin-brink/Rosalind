import os

input = open(os.getcwd() + r"\data\rosalind_fib.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read()
data = data.split(' ')

n = int(data[0])
k = int(data[1])

prev = 0
curr = 1

total = 0

for i in range(n-1):
	total = curr + prev*k

	print("{0}: {1} * {2:2} + {3:2} = {4:2}".format(i+1, k, prev, curr, total))
	
	prev = curr
	curr = total

print()
print('total:', str(total))
output.write(str(total))