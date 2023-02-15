# Program 19: writing files

log = True # switches between progam 19a and 19b

if log == True:
    writeFile = open("log.txt", "w")
    toLog = input("What do you want to write to the log?/n")
    writeFile.write(toLog)

    readDecision = input("Do you want to read back the log? yes/no")
    if readDecision == "yes":
        writeFile = open("log.txt", "r")
        print(writeFile.read())
        writeFile.close()
    else:
        writeFile.close()
else:
    file1 = open("file1.txt", "w") # w writes text to the file; may overwrite text if you aren't careful
    write = ["I \t love \t tabs!."]
    file1.writelines(write)
    file1.close()

    file1 = open("file1.txt", "a") # a appends text to the end of the file
    file1.write("Tabs are the coolest way to format your text!")
    file1.close()

    file1 = open("file1.txt", "r") # 'r' reads the file
    print("Outputs the text written in the document:")
    print(file1.read())
    file1.close()
