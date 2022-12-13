
import time
from pathlib import Path

import numbers

###Basics on each day
start_time = time.time()
#p = Path(__file__).with_name('example input.txt')
p = Path(__file__).with_name('input.txt')

##Part 1
total = 0
##code
def get_visible_from_edge(map,x,y):
    direction_arrays = {}
    index_array = {}
    directions = ['east','west','north','south']
    tree_number = map[x][y]
    length = len(map)
    direction_arrays['west'] = map[x][:y]
    direction_arrays['east'] = map[x][y+1:length]
    direction_arrays['north'] = [i[y] for i in map[:x]]
    direction_arrays['south']= [i[y] for i in map[x+1:length]]
    max_west = max(direction_arrays['west'])
    max_east = max(direction_arrays['east'])
    max_north = max(direction_arrays['north'])
    max_south = max(direction_arrays['south'])

    if min([max_west,max_east,max_north,max_south]) < tree_number:
        visible = 1
    else:
        visible = 0

    for direction in directions:
        if direction in ["north","west"]:
            direction_arrays[direction].reverse()
        ordinal = direction_arrays[direction]
        largest_trees = list(filter(lambda x: (x >= tree_number), ordinal)) 
        if len(largest_trees) > 0:
            max_ordinal = largest_trees[0]
            index_array[direction] = ordinal.index(max_ordinal) + 1
        else:
            max_ordinal = 0
            index_array[direction] = len(ordinal)
    answer = 1
    for k in index_array:
        answer = answer * index_array[k] 
    return visible,answer 

with open(p,'r') as file:
    result = [[x for x in line.strip()] for line in file]
    length = len(result)
    best_view = 0
    for i in range(0,length):
        for j in range(0, length):           
            if i in [0,length-1] or j in [0, length - 1]:
                total = total + 1
            else:
                calculation = get_visible_from_edge(result,i,j)
                total = total + calculation[0]
                best_view = max([best_view,calculation[1]])
print(total,best_view)
print("--- %s seconds ---" % (time.time() - start_time))
