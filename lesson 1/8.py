# Program 8: Boolean logic and comparisons

a = 6
b = 4
c = 17

# == checks if two values are equal
# != checks if two values are not equal
# < checks if the first value is less than the second value; > works in reverse
# <= checks if the first value is less than or equal to the second value; >= works in reverse

print(a == b and b == c) # and will check if both arguments are true
print(a == c and b != c)
print(a > b and b > c)
print(a == b or b == c)
print (a <= b or b <= c) # or will check if either argument is true
print(not a == b and b == c) # not will check if the argument is not true
