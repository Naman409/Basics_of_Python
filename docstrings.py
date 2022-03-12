class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    #   This is a docsting -It displays the string msg inside the method 
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

yakub = Person("Yakub")
help(yakub.greeting)