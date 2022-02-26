import os
from pprint import pprint as pp


def FASTAFormat(input_string):
	list = input_string.split('>')[1:] # First item is always blank (probably)

	fasta = dict()
	for line in list:
		lines = line.split('\n')
		fasta[lines[0]] = ''.join(lines[1:])

	return fasta


input = open(os.getcwd() + r"\data\rosalind_lcsm.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read()
fasta = FASTAFormat(data)

strings = list(fasta.values())

nucs = ['A', 'G', 'C', 'T']
possible = nucs[:]
longest = ''

while len(possible) > 0:
	not_found = []

	# check that each possible string is present
	for p in possible:
		for s in strings:
			if p not in s:
				not_found += [p]
				break
		else:
			longest = p


	# remove anything that wasnt found
	for item in not_found:
		possible.remove(item)

	# remake the list of possibilies by adding another nuc to the end
	new = list()
	for n in nucs:
		for p in possible:
			new += [p + n]
	possible = new[:]

print(longest)
output.write(longest)

input.close()
output.close()