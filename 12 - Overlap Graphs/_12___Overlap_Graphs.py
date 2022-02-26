import os
from pprint import pprint as pp


def FASTAFormat(input_string):
	list = input_string.split('>')[1:] # First item is always blank (probably)

	fasta = dict()
	for line in list:
		lines = line.split('\n')
		fasta[lines[0]] = ''.join(lines[1:])

	return fasta


input = open(os.getcwd() + r"\data\rosalind_grph.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read()
fasta = FASTAFormat(data)
pp(fasta)
print()

graph = list()
for key1 in fasta:
	for key2 in fasta:
		if key1 == key2:
			continue
		if fasta[key1][-3:] == fasta[key2][:3]:
			graph += [' '.join([key1, key2])]

pp(graph)
print()

print('\n'.join(graph))
output.write('\n'.join(graph))

input.close()
output.close()