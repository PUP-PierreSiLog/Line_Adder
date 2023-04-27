import sys
#Creates a file to append
#Create a method to write multiple line of text contents
def basic(line, choice):
    line=input("Enter line:")
    choice = input("Are there more lines? y/n")

#If loop for the variables
if "y" in choice:
    basic()
else:
    sys.exit()