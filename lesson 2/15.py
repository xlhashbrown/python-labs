# Program 15: for loops

colorList = ["blue", "red", "green", "yellow", "orange", "purple"]

print("My opinions on colors.")
for color in colorList:
    if color == "blue":
        print(str(color) + ": very good")
    elif color == "purple" or color == "orange":
        print(str(color) + ": alright")
    else:
        print(str(color) + ": yuck")
