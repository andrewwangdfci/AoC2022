
import time
from pathlib import Path

###Basics on each day
start_time = time.time()
p = Path(__file__).with_name('input.txt')

##Part 1
total = 0
##code
def badge_value(letter):

    ascii_code = ord(letter)
    if letter.isupper():
        value = (ascii_code - 38)
    else:
        value = (ascii_code - 96)
    return value

with open(p, 'r') as file:
    content = file.readlines()
    i = 0
    for line in content:
        i = i + 1
        rs_length = len(line.strip())
        rs_part_length = int(rs_length / 2)
        rs_1 = line[0:rs_part_length]
        rs_2 = line[rs_part_length:rs_length]
        rs_intersect = set(rs_1).intersection(rs_2)
        letter = list(rs_intersect)[0]
        letter_value = badge_value(letter)
        total = total + letter_value

print (total)

total = 0
##part 2
with open(p, 'r') as file:
    content = file.readlines()
    i = 0
    for line in content:
        elf_number = i % 3
        line_value = line.strip()

        if elf_number == 0:
            rs_compare = set(line_value)
        else:
            rs_compare = rs_compare.intersection(set(line_value))

        if elf_number == 2:
            letter = list(rs_compare)[0]
            letter_value = badge_value(letter)
            total = total + letter_value
            rs_compare = ""
        i = i + 1
    print(total)
print("--- %s seconds ---" % (time.time() - start_time))

