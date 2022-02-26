import os
from pprint import pprint as pp

input = open(os.getcwd() + r"\data\rosalind_iev.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read().split(' ')[0:6]
for i in range(6):
	data[i] = int(data[i])
pp(data)

# No reason to work this out programatically...it's static
# AA-AA -> 100% * 2 = 2
# AA-Aa -> 100% * 2 = 2
# AA-aa -> 100% * 2 = 2
# Aa-Aa ->  75% * 2 = 1.5
# Aa-aa ->  50% * 2 = 1
# aa-aa ->   0% * 2 = 0
offspring = [2, 2, 2, 1.5, 1, 0]

total = 0
for i in range(6):
	total += data[i] * offspring[i]

print(total)
output.write(str(total))

input.close()
output.close()