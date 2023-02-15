# Program 9: identity operators

a = 3
b = a # while they have the same value, variable b is still a different variable than variable a

northItems = ["raincoat", "snow boots"]
eastItems = ["umbrella", "sneakers"]

print(northItems == eastItems) # true because both variables have the same value
print(northItems is eastItems) # false because, while they have the same value, they are not linked to the same place in memory
print(northItems is not eastItems)

print(a == b) # true because the value of variable a is the same as the value of variable b
print (a is b) # true because variable a and variable b beacuse they point to the same value
