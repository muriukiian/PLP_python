import os

#file creation
myFile = open('my_file.txt', 'w')
myFile.write("This is a new file.")
myFile.write("\n It is an assignment.")
myFile.write("\n Take care of this file")
myFile.close()

#file reading and display
myFile = open('my_file.txt', 'r+')
print(myFile.read())
myFile.close()

#file appending
myFile= open('my_file.txt', 'a')
myFile.write("Python is easy to learn")
myFile.write("\nIt takes 20 hours to be good at something.")
myFile.write("\nJust do not quit on it.")
myFile.close()

#error handling
file_name= input("Enter file name: ")
try:
    file_open = open(file_name, 'r+')
    try:
      file_open.read()
    except:
       print("Something went wrong while trying to read the file.")
    finally:
       file_open.close()
except:
   print("Something went wrong when opening the file.")