class example():#class declaration
    def printer(self):
        print("hello how are you")
obj1 = example()#object creation
obj1.printer()#calling with object for the function.

#__init__ function

class example2:#initializing functions
    def __init__(self, name, age):
        self.name = name
        self.age = age
obj2 = example2("ADARSH",22)
print(obj2.name)