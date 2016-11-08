# ported to Python2
from sys import argv

script = argv
# gets the script name as an argument so python knows to operate on it

targetFile = raw_input("Create or open a file by typing a name: ")
# ^ creates a file by giving it a name, or opens one with a matching name
theFile = open(targetFile, 'r+')
# ^ allows the python to read and write the file, using 'w+' would erase the file's contents
print "This is the contents of", theFile.name
theFile.seek(0)
# sends the reaad cursor to the first line
print theFile.read()
# reads the file's contents from line 1 to the end, then prints it to the console

theAnswer = raw_input("Do you want to add anything to it (y/n)?")
# directs the program based on whether you want to add stuff, or leave the file as it is, without changes

if theAnswer == "y":
    clearTheFile = raw_input("Do you want to clear the file contents (y/n)?")
    if clearTheFile == "y":
        theFile.truncate(0)
        # erases the file contents
    else:
        print "Contents preserved."
        # ^ tells us the file contents weren't erased
    addThisToTheFile = raw_input("> ")
    if clearTheFile == "y":
        theFile.write(addThisToTheFile)
    else:
        theFile.write("\n"+addThisToTheFile)
        # add more than one line to the file
        continueWriting = raw_input("Add another line? (y/n)?")
        while continueWriting == "y":
            addThisToTheFile = raw_input(">")
            theFile.write("\n"+addThisToTheFile)
            continueWriting = raw_input("Add another line? (y/n)?")
    # ^ this IF choice just determines whether or not to put a blank line at the top of the file
    theFile.seek(0)
    # ^^ send the read cursor back to a specific line, in this case, line 0, so we can read the file again to see the new content added
    print "Here's the whole file, with your stuff added:"
    print theFile.read()
    # prints out the updated file contents
    print "I guess we're done here."
    theFile.close()
else:
    print "I guess we're done here."
    theFile.close()

# need to learn more about functions in python, to try condensing some of this code
