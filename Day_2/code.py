
import time
from pathlib import Path

###Basics on each day
start_time = time.time()
p = Path(__file__).with_name('input.txt')

##variables
i = 0
points = {}
points["A"] = 1 #Rock
points["B"] = 2 #Paper
points["C"] = 3 #Scissors
points["X"] = 1 #Rock
points["Y"] = 2 #Paper
points["Z"] = 3 #Scissors
points["W"] = 6
points["L"] = 0
points["D"] = 3
total = 0

##code
with open(p, 'r') as file:
    content = file.readlines()
    for line in content:
        you = line[-2].strip()
        opponent = line[:1].strip()
        results = points[opponent] - points[you]
        
        match abs(results):
            case 0:
                outcome_points = "D"
            case 1:
                if results < 0:
                    outcome_points = "W"
                else:
                    outcome_points = "L"
            case _:
                if results > 0:
                    outcome_points = "W"
                else:
                    outcome_points = "L"
        total = total + points[you] + points[outcome_points]
print(total)

total = 0
with open(p, 'r') as file:
    content = file.readlines()
    for line in content:
        outcome_requirement = line[-2].strip()
        opponent = line[:1].strip()
        match outcome_requirement:
            case "X":
                outcome_required = "L"
                you = points[opponent] - 1
                if you == 0:
                    you = 3
            case "Y":
                outcome_required = "D"
                you = points[opponent]
            case "Z":
                outcome_required = "W"
                you = (points[opponent] % 3) + 1 

        total = total + you + points[outcome_required]
print(total)
print("--- %s seconds ---" % (time.time() - start_time))

