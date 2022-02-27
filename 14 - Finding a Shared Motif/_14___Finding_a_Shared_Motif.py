import os
from pprint import pprint as pp


def FASTAFormat(input_string):
	list = input_string.split('>')[1:] # First item is always blank (probably)

	fasta = dict()
	for line in list:
		lines = line.split('\n')
		fasta[lines[0]] = ''.join(lines[1:])

	return fasta


def OrderShort(strings):
	for i in range(len(strings)):
		for j in range(i+1, len(strings)):
			if len(strings[j]) < len(strings[i]):
				temp = strings[j]
				strings[j] = strings[i]
				strings[i] = temp
	return strings


input = open(os.getcwd() + r"\data\rosalind_lcsm.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read()
fasta = FASTAFormat(data)

strings = list(fasta.values())
strings = OrderShort(strings)

shortest = strings[0]
strings = strings[1:]
longest = ''

# iterate for size
for i in range(1, len(shortest)): 

	new_found = False
	# iterate over the string
	for j in range(len(shortest) - i):
		# iterate over each string
		for s in strings:
			if shortest[j:j+i] not in s:
				break
		else:
			longest = shortest[j:j+i]
			new_found = True
			break
		if new_found:
			break

print(longest)
output.write(longest)

input.close()
output.close()