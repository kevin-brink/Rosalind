import os
from pprint import pprint as pp


def find_GC_content(strand):
	content = 0
	for n in strand:
		if n in ["C", "G"]:
			content += 1

	return content / len(strand)

input = open(os.getcwd() + r"\data\rosalind_gc.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read()
data = data.split('>')
data.remove('')


db = dict()
for dna in data:
	items = dna.splitlines()

	name = items[0]
	items = items[1:]
	
	strand = ''
	for n in items:
		strand += n

	db[name] = find_GC_content(strand) * 100

pp(db)

max = 0
answer = ''

for key in db.keys():
	if db[key] > max:
		max = db[key]
		answer = key

output.write(
	"{0}\n{1}".
	format(answer, db[answer])
	)

print(
	"\n{0}\n{1}".
	format(answer, db[answer])
	)

output.close()