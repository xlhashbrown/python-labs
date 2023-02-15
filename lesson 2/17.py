# Program 17: nested for loops

import random
initialGoal = 5
multiplier = random.randint(1,8)
offWeek = True

for weeklyGoal in range(1,52):
    if weeklyGoal%4 == 0 and offWeek == True:
        print("Take a break this week.")
        continue
    multiplier
    weeklyRidingGoal = initialGoal * multiplier
    print("You should bike about " + str(weeklyRidingGoal) +  " miles this week.")
    for averageDaily in range(1,8):
        print("Try to bike about " + str(weeklyRidingGoal/7) + " miles each day.")
