file=open("data.json","r",500)
content = file.read()
#print(content)
file.close()

#open files for writing
file2 = open("file.txt", "w")
file2.write("This is America - Childish Gambino\n")
file2.close()

#open files for appending
file2 = open("file.txt", "a")
file2.write("African Giant - Burna Boy")
file2.close()