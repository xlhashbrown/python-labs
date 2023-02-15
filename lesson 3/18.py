# Program 18: read and readline

fullRead = False # switches between program 18a and 18b

if fullRead == True:
    workFile = open("jackets.txt", "r")
    workFileContents = workFile.read()
    print(workFileContents)
    workFile.close()
    print("The file has been closed.")
else:
    workFile = open("jackets.txt", "r")
    workFileFirstLine = workFile.readline()
    print(workFileFirstLine)
    workFileSecondLine = workFile.readline()
    print(workFileSecondLine)
    workFile.close()
    print("The file has been closed.")
