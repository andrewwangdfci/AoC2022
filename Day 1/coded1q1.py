import os

file_path = r'C:\Users\aw1022\OneDrive - Mass General Brigham\Load to PGRES\Advent of Code\inputd1q1.txt'

f = open(file_path, 'r')
content = f.readlines()

i = 0
elf = {0:0}
for line in content:
    if line.strip() == "":
        i += 1
        elf[i] = 0
    else:
        elf[i] = elf[i] + int(line)
f.close()       
print(max(elf.values()))

elf_top_three = sorted(elf, key=elf.get, reverse=True)[:3]

amount = 0
for elves in elf_top_three:
    amount = amount + elf[elves]

print(amount)

