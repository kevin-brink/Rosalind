import os

input = open(os.getcwd() + r"\data\rosalind_revc.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read()
reverse_data = ""
answer = ""

n_map = {
	"A": "T",
	"T": "A",
	"C": "G",
	"G": "C"
	}

for n in range(len(data), 0, -1):
	reverse_data += data[n-1]

for n in reverse_data:
	if n in ["A", "T", "C", "G"]:
		answer += n_map[n]

output.write(answer)

print(data)
print(reverse_data)
print(answer)