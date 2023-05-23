#inheritance without extra methodes 

class test:
    def __init__(self,object1):
        self.object1=object1

class child(test):
    pass

output=child("Hello")
print(f'{output.object1}\n')

#inheritance with extra methodes 
class test_two:
    def __init__(self,message):
        self.message=message

class child_two(test_two):
    def __init__(self, message,name):
        super().__init__(message)
        self.__name=name
    def get_name(self):
        return self.__name 

output=child_two("Hello","charlie")
print(f'{output.message} {output.get_name()}\n')

#Polymorphism

class friuts:
    def __init__(self,fruitname,price,weight):
        self.__fruitname=fruitname
        self.__price=price
        self.__weight=weight
    def name(self,):
        return self.__fruitname

class peds:
    def __init__(self,pedname,age):
        self.__pedname=pedname
        self.__age=age
    def name(self):
        return self.__pedname

class vegetable:
    def __init__(self,vegetablename,healthy,weight):
        self.__vegetablename=vegetablename
        self.__healthy=healthy
        self.__weight=weight
    def name(self):
        return self.__vegetablename

#name, price in cents, 
apple=friuts("apple",300,100)
#name, age in years
dog=peds("Dog",2)
#name, healthy yes/no in boolean, weigth in gramm
tomato=vegetable("Tomato",True,100)

print(f'the fruit that i pic is a {apple.name()}, the pet i pic is a {dog.name()}, the vegetable i pic is a {tomato.name()}')
