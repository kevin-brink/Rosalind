import os
from pprint import pprint as pp


def PhenotypeProbability(p1='TT', p2='tt', p='T'):
	hits = 0
	total = 0

	phen = {'k': 'TT', 'm': 'Tt', 'n':'tt'}
	p1 = phen[p1]
	p2 = phen[p2]

	for i in p1:
		for j in p2:
			total += 1
			if 'T' in [i, j]:
				hits += 1

	return hits/total



input = open(os.getcwd() + r"\data\rosalind_iprb.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read().split(' ')
k = int(data[0])
m = int(data[1])
n = int(data[2])
t = k + m + n

print('k:', k)
print('m:', m)
print('n:', n)
print('t:', t)


# Create a probability dictionary to determine the odds of dominant trait for given parent phenotypes
p_matrix = dict()
for i in ['k', 'm', 'n']:
	temp = dict()
	for j in ['k', 'm', 'n']:
		temp[j] = PhenotypeProbability(i, j)
	p_matrix[i] = temp

print('    {0:8}{1:8}{2:8}'.format('k', 'm', 'n'))
for i in p_matrix.keys():
	line = i + ': '
	for j in p_matrix[i].keys():
		line += '{0:8}'.format(p_matrix[i][j])
	print(line)

print(p_matrix['m']['n'])


# Create a probability dictionary to determine the odds of any two phenotypes mating
parents = {'k': k, 'm': m, 'n': n}

x = {
	'k': { 'k' : k-1, 'm': m,   'n': n   },
	'm': { 'k' : k,   'm': m-1, 'n': n   },
	'n': { 'k' : k,   'm': m,   'n': n-1 }
	}

x_matrix = dict()
for i in {'k', 'm', 'n'}:
	temp = dict()
	for j in {'k', 'm', 'n'}:
		temp[j] = (parents[i] / t) * (x[i][j] / (t-1))
	x_matrix[i] = temp
pp(x_matrix)

# Calculate actual odds of dominant trait given two random parents
chance = 0
for i in x_matrix.keys():
	for j in x_matrix[i].keys():
		chance += p_matrix[i][j] * x_matrix[i][j]

print()
print(chance)

output.write(str(chance))

input.close()
output.close()