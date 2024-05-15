from classeg import example2 #importing the the class from previous file using the concept of inheritance a class can be imported from another class and used in another class
class example3(example2):
    pass #just used to pass the execution without any error
obj3 = example2("name",21)
print(obj3.name)
