# Program 5: variables and type casting
price = 3.95
bananas = 5

print("The price is $", price, "for a pound of bananas.")
price = 3.45
print("Now on sale! The price is now $",price,"per pound.")
print("The toal price for all of the bananas available is $", (price * bananas), ".")

print("The type of price is", type(price))
print("The type of bananas is", type(bananas))

print("If the price was an integer, it would be", int(price), ".")
print("If bananas were a floating point, it would be", float(bananas), ".")