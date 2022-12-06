
import time
from pathlib import Path
import re


###Basics on each day
start_time = time.time()
p = Path(__file__).with_name('initial.txt')
q = Path(__file__).with_name('input.txt')
#p = Path(__file__).with_name('example.txt')

##Part 1
total = 0
##code


arrangement = []
buckets = {}

def get_stacks(p):
    with open(p,'r') as file:
        content = file.readlines()
        for line in content:
            i = 0
            line = line.rstrip('\n')
            line_length= len(line)+4
            for baskets in range(0,line_length,4):
                value = line[baskets-4:baskets].strip()
                if i not in buckets.keys():
                    buckets[i] = []
                if  value != '':    
                    buckets[i].insert(0,value)
                i = i + 1
        del buckets[0]
        return buckets

def put_movement(stacks,move_amount, from_stack, to_stack):
    move_amount = int(move_amount)
    from_stack = int(from_stack)
    to_stack = int(to_stack)
    from_amount_start = len(stacks[from_stack])-1
    from_amount_end = from_amount_start - move_amount
    print(move_amount)
    for idx in range(from_amount_start,from_amount_end,-1):
        stacks[to_stack].append(stacks[from_stack].pop(stacks[from_stack].index(stacks[from_stack][idx])))
    return stacks

def get_last_item(stacks):
    last_element = []
    for i in stacks:
        last_element.append(stacks[i][-1])
    return last_element

stacks = get_stacks(p)

with open(q,'r') as file:
    content = file.readlines()
    i = 1
    for line in content:
        re_line = line.strip().replace("move ","").replace(" from ",";").replace(" to ",";").split(";")
        stacks = put_movement(stacks,re_line[0],re_line[1],re_line[2])
        i = i + 1
        print(re_line[0],re_line[1],re_line[2],stacks)
        if i > 4:
            print(get_last_item(stacks))
            quit()
    print(stacks)
    print(get_last_item(stacks))
print("--- %s seconds ---" % (time.time() - start_time))
