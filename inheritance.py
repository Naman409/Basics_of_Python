class Fruit():
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
# This is how we inherit in python
class Apple(Fruit):
    pass

class Grapes(Fruit):
    pass

mummy = Apple("Red","Sweet")
papa = Apple("Green","Tart")

print(mummy.color)
print(mummy.flavor)