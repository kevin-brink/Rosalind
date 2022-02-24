import os
from pprint import pprint as pp

input = open(os.getcwd() + r"\datasets\rosalind_dna.txt", "rt")
output = open(os.getcwd() + r"\datasets\output.txt", "wt")

sample = input.read()
print(sample)

nucs = {
	"A" : 0,
	"C" : 0,
	"G" : 0,
	"T" : 0
	}

for l in sample:
	try:
		nucs[l] += 1
	except:
		pass

for n in nucs.keys():
	print("'{0}': {1}".format(n, nucs[n]))

output.write("{0} {1} {2} {3}".format(nucs['A'], nucs['C'], nucs['G'], nucs['T']))