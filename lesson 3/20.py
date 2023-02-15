# Program 20: OS module

import os

if os.path.isfile("log.txt"):
    writeFile = open("log.txt", "a")
else:
    writeFile = open("log.txt", "w")

toLog = input("What do you want to write to the log?\n")
writeFile.write("\n" + toLog) # avoids overwritng by pushing all new text to the next line
writeFile.close()
