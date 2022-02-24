import os

input = open(os.getcwd() + r"\data\rosalind_rna.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read()
answer = ""

for n in data:
	if n == "T":
		answer += "U"
	elif n in ["A", "C", "G"]:
		answer += n

print(data)
print(answer)

output.write(answer)