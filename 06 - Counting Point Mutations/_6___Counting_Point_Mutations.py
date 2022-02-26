import os

input = open(os.getcwd() + r"\data\rosalind_hamm.txt", "rt")
output = open(os.getcwd() + r"\data\output.txt", "wt")

data = input.read()
datasets = data.splitlines()

# Confirm data is split correctly
for line in datasets:
	print('>>> ' + line + ' : ' + str(len(line)))
print()

count = 0
for i in range(len(datasets[0])):
	if datasets[0][i] != datasets[1][i]:
		count += 1

print(count)
output.write(str(count))

input.close()
output.close()