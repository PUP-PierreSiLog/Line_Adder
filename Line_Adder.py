import sys
#Creates a file to write
with open("D:\[CMPE103] OOP\Line_Adder\\mylife.txt", "w") as source:
    #Create a method to write multiple line of text contents
    init=input("Welcome to the program! Are you ready to start? y/n")

    #While loop for the variables
    while "y" in init.lower():
        line=input("Enter line:")
        source.write(line+"\n")
        choice = input("Are there more lines? y/n")
        if "y" in choice.lower():
            source.write(choice+"\n")
            continue
        else:
            sys.exit()
    else:
        sys.exit()