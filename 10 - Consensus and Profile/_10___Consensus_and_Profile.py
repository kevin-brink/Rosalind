import os
from pprint import pprint as pp

def ToString(n, i_list):
	string = n + ':'
	for i in i_list:
		string += ' ' + str(i)

	return string


input = open(os.getcwd() + r"\data\rosalind_cons.txt", "rt")
output = open(os.getcwd() + r"\data\output.info", "wt")

data = input.read()
data = data.split('>')[1:]

set = dict()
set_list = list()
size = 0
for point in data:
	list = point.splitlines()
	line = ''.join(list[1:])
	set[list[0]] = line
	set_list += [line]
	size = len(line)

pp(set)

consensus_matrix = {'A': [], 'C': [], 'G': [], 'T': []}

# for each position
# for each base
# for each string

print()
print (' A | C | G | T | Final')
consensus_string = ''
for i in range(size):
	total = 0
	for n in ['A', 'C', 'G', 'T']:
		count = 0
		for line in set_list:
			if line[i] == n:
				count += 1
				total += 1
		consensus_matrix[n] += [count]

	max = 0
	curr = ''
	for n in ['A', 'C', 'G', 'T']:
		if consensus_matrix[n][i] >= max:
			max = consensus_matrix[n][i]
			curr = n
	consensus_string += curr

	print('{0:2} |{1:2} |{2:2} |{3:2} | {4:2} : {5}'.format(
		consensus_matrix['A'][i], 
		consensus_matrix['C'][i], 
		consensus_matrix['G'][i], 
		consensus_matrix['T'][i], 
		total, curr
		)
	)

print()

a_string = ToString('A', consensus_matrix['A'])
c_string = ToString('C', consensus_matrix['C'])
g_string = ToString('G', consensus_matrix['G'])
t_string = ToString('T', consensus_matrix['T'])

print(consensus_string)
print(a_string)
print(c_string)
print(g_string)
print(t_string)

output.writelines('\n'.join([consensus_string, a_string, c_string, g_string, t_string]))

input.close()
output.close()