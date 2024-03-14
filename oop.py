#Create a Python class named Person.
class Person:
  def __init__(self, name, age, gender, complexion):
    self.name=name
    self.age=age
    self.gender=gender
    self.complexion=complexion
#Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
  def introduce(self):
    print(f'Name: {self.name} Age: {self.age} Gender: {self.gender} ')

class African(Person):
  def __init__(self, name, age, gender, complexion):
    self.name=name
    self.age=age
    self.gender=gender
    self.complexion=complexion
  def isAfrican(complexion):
    if complexion == 'Black':
      print('This is an African')
    elif complexion == 'White':
      print('This is caucasian')
    else:
      print('Indian')


#Create an instance of the Person class and call the introduce method to display the person's information.
person = Person("Ian",27,"Male", "Monk")
person.introduce()
african = African("Ian", 27, "Male", "Black")
print(african.isAfrican())
african.introduce()
