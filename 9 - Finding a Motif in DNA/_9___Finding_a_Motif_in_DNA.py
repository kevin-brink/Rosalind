import os

input = open(os.getcwd() + r"\data\rosalind_subs.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

dna = input.readlines(1)[0].removesuffix('\n')
motif = input.readlines(1)[0].removesuffix('\n')

print(dna, motif)

matches = []
for i in range(len(dna)):
	if dna[i] == motif[0]:
		for j in range(len(motif)):
			if i+j < len(dna) and dna[i+j] != motif[j]:
				break
		else:
			if dna[i:i+len(motif)] == motif:
				matches += [i+1]

s_matches = ''
for i in matches:
	s_matches += str(i) + ' '
s_matches.removesuffix(' ')

print(matches)
print(s_matches)
output.write(s_matches)

input.close()
output.close()
