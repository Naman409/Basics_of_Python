# This is how we create a class. First alphabet of the class name must be capital 
class Apple:
    color = ""
    flavor = ""

# This is the way to create an object of class apple
firstobject = Apple()

firstobject.color = "red"
firstobject.flavor = "sweet"

secondobject = Apple()

secondobject.color = "golden"
secondobject.flavor = "creamy"

print("Color of first object is {} and flavor of second object is {}".format(firstobject.color,secondobject.flavor))