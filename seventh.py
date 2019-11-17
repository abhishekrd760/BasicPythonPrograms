class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print("the first name is ",self.firstname, "the last name is ",self.lastname)

class Student(Person):
  pass


x = Student("Potato","Salad")
x.printname()