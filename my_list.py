#Create an empty list called my_list.
my_list = []
#Append the following elements to my_list: 10, 20, 30, 40.
list_2 = [10,20,30,40]
for i in list_2: my_list.append(i)
#Insert the value 15 at the second position in the list.
my_list.insert(1,15)
#Extend my_list with another list: [50, 60, 70].
my_list.extend([50,60,70])
#Remove the last element from my_list.
del my_list[-1]
#Sort my_list in ascending order.
my_list.sort()
#Find and print the index of the value 30 in my_list
print(my_list.index(30))