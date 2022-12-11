
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

directory_list = {"size":0}
directory = []


def get_current_directory(string):
    current_directory = directory_list
    for items in string:
        current_directory = current_directory[items]
    return current_directory

def put_directory_size(string,value):
    current_directory = directory_list
    for items in string:
        current_directory = current_directory[items]
        current_directory["size"] = current_directory["size"] + value
    directory_list["size"] = directory_list["size"] + value

def get_folder_size(d,value):
    for k, v in d.items():
        if isinstance(v, dict):
            if d[k]["size"] <= value:
                array_list.update({k:d[k]["size"]})
            get_folder_size(v,value)
    return array_list

def get_folder_size_gt(d,value):
    for k, v in d.items():
        if isinstance(v, dict):
            if d[k]["size"] >= value:
                array_list.update({k:d[k]["size"]})
            get_folder_size_gt(v,value)
    return array_list

array_list = {}
with open(p,'r') as file:
    content = file.readlines()
    for line in content:
        line = line.strip()
        line_action = line.split(" ")
        if line_action[0] == "$":
            if line_action[1] == "cd":
                if line_action[2] == "/":
                    directory = []
                elif line_action[2] == "..":
                    directory.pop()
                else:
                    directory.append(line_action[2])
            elif line_action[1] == "ls":
                current_directory = get_current_directory(directory)
        else:
            if line_action[0].isnumeric():
                put_directory_size(directory,int(line_action[0]))
            else:
                current_directory.update({line_action[1]: {"size":0}})
print(directory_list)
print(sum(get_folder_size(directory_list,100000).values()))

array_list = {}
remaining_space = 70000000 - directory_list['size']
space_needed = 30000000 - remaining_space

d = get_folder_size_gt(directory_list,space_needed)
print(min(d.values()))
print("--- %s seconds ---" % (time.time() - start_time))
