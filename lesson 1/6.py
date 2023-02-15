# Program 6: Making lists
names = ["Peter", "George", "Micheal", "Johnny"]

for name in names:
    print(name) # this for loop makes a variable "name" out of each string in the list "names"; each time it repeats, it overwrites the previous value of the variable "name"

print() # starts a new line for every repeat
names.append("James") # while a list can be appended, a variable can not
names.remove("George")
names.sort() # sort will sort strings by alphabetical order

for name in names:
    print(name)
