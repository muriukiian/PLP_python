#lists
list_a = [42,3,56,67,'89']
print(list_a[0])
list_a[0] = 10
print(list_a[0])
#to get length of a list
print(len(list_a))
#inserting a value at a particular index
list_a.insert(len(list_a), 89) #inserts 89 at the index 5
print(list_a)
list_a.insert(2, 78)  #inserts 78 at the index 2
print(list_a)
#appending a value at the end of the list
list_a.append(45)
print(list_a)
#appending a list to the end of the current list
list_a.extend([45,67,43,67])
print(list_a)
#to know the total number of a particular item in a list
print(list_a.count(45))
#to delete a value in a specified index from the list
list_a.pop(6)  #deletes the value at index 6
print(list_a)
del list_a[8] #deletes the value at index 8
print(list_a)

for item in list_a:
  print(item)

numbers = [number ** 2 for number in range(1,11)]
print(numbers)


#tuples ==> similar to lists but we cannot change the content of a tuple once assigned.
#tuples are immutable. Also tuples support duplicity of values like in lists.
var_1 = ("hello",)  #creating a tuplewith one value. Notice the comma after "hello"
print(type(var_1))

#Accessing tuple elements using indexing
alphabets = ('e','f','g','y','r','p','s','c','h')
print(alphabets[2])  #prints g
print(alphabets[5])  #prints p
print("==========")
#Negative indexing
alphabets = ('e','f','g','y','r','p','s','c','h')
print(alphabets[-1])  #prints h
print(alphabets[-5])  #prints r
print(alphabets[-6])  #prints y
#Tuple methods
#count method counts the number of an item in a tuple
alphabets = ('e','f','g','y','r','p','s','f','c','g','h')
print(alphabets.count('f'))  #prints 2
print(alphabets.count('g'))  #prints 2
#index method prints the index of the first occurrence of an item in a tuple
alphabets = ('e','f','g','y','r','p','s','f','c','g','h')
print(alphabets.index('f'))  #prints 1
print(alphabets.index('g'))  #prints 2

#DICTIONARIES
print("DICTIONARIES")
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city['Nepal'])
#Add elements to a python dictionary
capital_city['Japan'] = 'Tokyo'
print(capital_city.keys())
print(capital_city.values())
#Changing values in a python dictionary
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
capital_city['England'] = 'Manchester'
print(capital_city['England'])
print(capital_city)
#Accessing elements from a dictionary
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city['England']) #prints London
#Removing elements from a dictionary
del capital_city['Nepal']  #deletes Nepal
print(capital_city)
#iterating throug a dictionary
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
for i in capital_city:
  print(f'The capital city of {i} is {capital_city[i]}.')


#sets cannot print out duplicates.
#create a set of integer type
studentId = {34,56,7,89,89}
print('Student ID: ', studentId)

#create a set of sting type
vowelLetters = {'a','e','i','o','u'}
print('Vowel letters: ', vowelLetters)

#create a mixed set
mixedSet = {'a', True, 45, 45.54}
print('Mixed set: ', mixedSet)

#create a set with duplicates and print out the set
mySetc= {2,3,4,55,55,55,5,5,6,7,9}
print(mySetc)

#adding elements into a set
mixedSet = {'a', True, 45, 45.54}
mixedSet.add(False)
print(mixedSet)

#Updating a set
brands = {'Gucci', 'Fendi', 'McQueen'}
brands2 = {'Nike', 'Adidas', 'Jordan'}
brands.update(brands2)
print(brands)

#for i in range(0,6):
 # print("*"*i)