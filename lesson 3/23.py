# Program 23: more formatting

alternate = False # switches between program 23a and 23b

if alternate == False:
    price = 3.95
    bananas = 5
    msg = print("The price is ${price: .2f} for a pound of bananas.")
    
    print(f"We have {bananas} pounds of bananas in stock.")
    print(msg.format(price=4))
else:
    named = "My name is {name}, I'm {age} years old.".format(name = "Logan", age = 17) # placeholders can be named, numbered, or left blank
    numbered = "My name is {0}, I'm {1} years old.".format("Logan", 17)
    blank = "My name is {}, I'm {} years old.".format("Logan", 17)

    print(named)
    print(numbered)
    print(blank)
