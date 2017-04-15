import os
# firstly we have to open the old file in read mode and the new file in write mode
oldfile=open("c:/myfile.txt","r")
newfile=open("c:/new file.txt","w")

# now using .write function
newfile.write(oldfile.read())
# now how to read this new file;
# firstlyclose the new file with
newfile.close()
# then
newfile=open("c:/new file.txt","r")
newfile.read()
# now how to rename;
# for this we have to import os(operating system)
# then os.rename('the name of file which have to be renamed','the new name of that file')    {with location}
# similarly we can remove any file with os.remove operator
# os.remove(the name and location of file which have to be raemoved)