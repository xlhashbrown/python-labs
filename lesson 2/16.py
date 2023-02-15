# Program 16: using pass

from random import randint

cash = randint(0,30)
print("You have $" + str(cash) + " on you.")
print("You hear a man on the sidewalk ask: 'Spare change?'")
if cash <= 5:
    print("He looks at your wallet. 'Wow, my bad. You're poor.'")
    print("You don't need someone else to call you poor, you already know that. You tear up a bit and walk away.")
elif cash > 5 and cash <= 20:
    print("He looks at your wallet. 'I know you've got some cash to spare.'")
    print("You give him some cash and walk away, feeling good about yourself.")
else:
    pass
