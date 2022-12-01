
file = open('input.txt', 'r')
lines = file.readlines()

elves = {
    0: 0,
}

elf_index = 0

for line in lines:
    line = line.strip()
    if line == '':
        elf_index += 1
        elves[elf_index] = 0
    else:
        elves[elf_index] += int(line)

sorted_values = sorted(elves.values())

print(f'Highest: {sorted_values[len(sorted_values)-1]}')

top_3_total = sorted_values[len(sorted_values)-1] + \
    sorted_values[len(sorted_values)-2] + \
    sorted_values[len(sorted_values)-3]

print(f'Top 3 total: {top_3_total}')
