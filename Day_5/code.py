
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


def get_stacks(p):
    buckets = {}

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
                    buckets[i].insert(0,value.replace("[","").replace("]",""))
                i = i + 1
        del buckets[0]
        return buckets

def put_movement(stacks,move_amount, from_stack, to_stack,direction):
    move_amount = int(move_amount)
    from_stack = int(from_stack)
    to_stack = int(to_stack)
    if direction < 0:
        from_amount_start = len(stacks[from_stack]) - 1
        from_amount_end = from_amount_start - move_amount
        for idx in range(from_amount_start,from_amount_end,direction):
            stacks[to_stack].append(stacks[from_stack].pop(idx))
    else:
        from_amount_end = len(stacks[from_stack])
        from_amount_start = from_amount_end - move_amount
       ##print(stacks[from_stack],move_amount,from_amount_start,from_amount_end,stacks[from_stack][from_amount_start])
        for idx in range(from_amount_start,from_amount_end,direction):
            stacks[to_stack].append(stacks[from_stack].pop(from_amount_start))    
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
        stacks = put_movement(stacks,re_line[0],re_line[1],re_line[2],-1)
        i = i + 1
    print(get_last_item(stacks))

stacks = {}
p = Path(__file__).with_name('initial.txt')
q = Path(__file__).with_name('input.txt')

stacks = get_stacks(p)

with open(q,'r') as file:
    content = file.readlines()
    i = 1
    for line in content:
        re_line = line.strip().replace("move ","").replace(" from ",";").replace(" to ",";").split(";")
        stacks = put_movement(stacks,re_line[0],re_line[1],re_line[2],1)
        i = i + 1
    print(get_last_item(stacks))

print("--- %s seconds ---" % (time.time() - start_time))
