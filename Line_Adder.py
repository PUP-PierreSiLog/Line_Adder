import sys
#Creates a file to write
with open("D:\[CMPE103] OOP\Line_Adder\\mylife.txt", "w") as source:
    #Create a method to write multiple line of text contents
    line=input("Enter line:")
    choice = input("Are there more lines? y/n")

    #While loop for the variables
    while "y" in choice:
        line=input("Enter line:")
        choice = input("Are there more lines? y/n")
    else:
        sys.exit()