#Create a Python class named Person.
class Person:
  def __init__(self, name, age, gender):
    self.name=name
    self.age=age
    self.gender=gender
#Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
  def introduce(self):
    print(f'Name: {self.name} Age: {self.age} Gender: {self.gender} ')

#Create an instance of the Person class and call the introduce method to display the person's information.
person = Person("Ian",27,"Male")
person.introduce()