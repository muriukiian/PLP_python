name = input('What is your name? ')
age = input('What is your age? ')
location = input('What is your location? ')

print(f'Hello {name}, you are {age} years old and live in {location}.')

#n = 0
#sum = 0
#while n <= 10:
#  sum += n
#  print(sum)
#  n = n + 1
#else:
#  print('n is greater than 10')

list_1 = [1,2.4,3.5,'dog',4,5,6]
new_list = []
for i in list_1:
  if type(i) in (str, float):
    new_list.append(i)

print(new_list)