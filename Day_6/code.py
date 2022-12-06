
import time
from pathlib import Path
import re


###Basics on each day
start_time = time.time()
#p = Path(__file__).with_name('example input.txt')
p = Path(__file__).with_name('input.txt')

##Part 1
total = 0
##code


with open(p,'r') as file:
    content = file.readlines()
    i = 1
    for line in content:
        line_count = len(line) + 1
        line = line.strip()
        for i in range (4,line_count,1):
            marker_set = set(line[i-4:i])
            if  len(marker_set)== 4:
                print("part 1:",i)
                break

        for i in range (14,line_count,1):
            marker_set = set(line[i-14:i])
            if  len(marker_set) == 14:
                print("part 2:",i)
                break

print("--- %s seconds ---" % (time.time() - start_time))
