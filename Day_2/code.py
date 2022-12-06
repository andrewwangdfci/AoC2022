
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
total_1 = 0
total_2 = 0
points_array = [3,1,2]

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

        opponent = line[:1].strip()
        match you:
            case "X":
                outcome_required = "L"
                you_points = points_array[points[opponent] - 1]
            case "Y":
                outcome_required = "D"
                you_points = points[opponent]
            case "Z":
                outcome_required = "W"
                you_points = (points[opponent] % 3) + 1 
        total_1 = total_1 + points[you] + points[outcome_points]
        total_2 = total_2 + you_points + points[outcome_required]
print(total_1)
print(total_2)

print("--- %s seconds ---" % (time.time() - start_time))

