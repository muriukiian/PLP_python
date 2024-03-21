

students = {'Nora':15, 'Gino':30}
name = input("Enter your name: ")
try:
  if names in students:
    print(f'{name}, you are {students[name]} years old.')
except NameError:
  print("Variable names is not defined. Please check your code.")
except:
  print("Something else went wrong")