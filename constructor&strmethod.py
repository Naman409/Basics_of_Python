class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
    # This str method below helps us to call the method directly with the help of object name
    # If this is not used the print(jonagold) will print memory address with a weird message
    def __str__(self):
        return "This apple is {} and its color is {}".format(self.color,self.flavor)

jonagold = Apple("red","sweet")

print(jonagold)