
import time
from pathlib import Path

###Basics on each day
start_time = time.time()
p = Path(__file__).with_name('input.txt')
#p = Path(__file__).with_name('example.txt')

##Part 1
total = 0
##code

with open(p, 'r') as file:
    content = file.readlines()
    subset_count = 0
    intersect_count = 0
    try_Two = 0
    j = 0
    for line in content:
        input = line.strip()
        pairs = list(input.split(","))

        for i in range(0,2):
            pairs[i] = pairs[i].split("-")
        
        one_one = int(pairs[0][0])
        one_two = int(pairs[0][1])
        two_one = int(pairs[1][0])
        two_two = int(pairs[1][1])


        first = range(one_one,one_two + 1)
        second = range(two_one,two_two + 1)       

        if(set(first).issubset(second) or set(second).issubset(set(first))):
            subset_count = subset_count + 1

        intersect = len(set(first).intersection(second))
        if (intersect > 0):
            intersect_count = intersect_count + 1
    print("subset:",subset_count)
    print("intersect:",intersect_count)
print("--- %s seconds ---" % (time.time() - start_time))
