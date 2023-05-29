import os
import pandas as pd

def MainMenu(Heading,inputtext,*entries):
    print(f'\n##{Heading}##')
    #here you can type whatever entry start number you want
    entrynumber=0
    #prints the entrynames with its numbers 
    for x in entries:
        print(f'\n{entrynumber+1} {entries[entrynumber]}')
        entrynumber+=1
        if x == entrynumber:
           break
    #check if input can be choosen or if it is out of range
    while True:
        choosennumber=input(f'\n{inputtext} : ')
        choosennumber=int(choosennumber)
        if choosennumber >choosennumber-choosennumber and choosennumber <= entrynumber:
             return choosennumber
        else:
            print("please try again! number can not be choosen")

#character class for comming features
class character():
    def __init__(self,name,lastname,age):
        self._name=name
        self._lastname=lastname
        self._age=age
    #name functions
    def get_name(self):
        return self._name
    
    def change_name(self,newname):
        self._name=newname
        return self._name
    #lastnamefunctions
    def get_lastname(self):
        return self._lastname
    
    def change_lastname(self,newlastname):
        self._name=newlastname
        return self._lastname
    #age functions
    def get_age(self):
        return self._age
        
    def change_age(self,newage):
        self._name=newage
        return self._age
 
#Create New Character Menu
def New(Heading):
    while True:
        print(f'\n##{Heading}##')
        name=input('\nGive the Character a name : ')
        lastname=input('\nGive the Character a Lastname : ')
        age=input('\nGive the Character a age : ')
        print(f'\nYour Character Name is {name} {lastname} and the age of the Character is {age}\n')
        check=input('is that correct? y=yes, n=no : ')
        element=name.lower()
        if check == "y":
            element=character(name,lastname,age)
            if os.path.exists('charactersaves.csv'):
                file=open('charactersaves.csv', 'a')
                file.write(f'\n{element.get_name()},{element.get_lastname()},{element.get_age()}')
                file.close
                tryagain=input('\nDo you want to create another Character? y=yes, n=no : ')
                if tryagain=="y":
                    pass
                elif tryagain=="n":
                    break
            else:
                file=open('charactersaves.csv', 'w')
                file.write("name,lastname,age")
                file.write(f'\n{element.get_name()},{element.get_lastname()},{element.get_age()}')
                file.close
                break
        
#Loading Existing Character into Table
def Load(Heading):
    print(f'\n##{Heading}##')
    if not os.path.exists('charactersaves.csv'):
        print(f'you have no Charaters createtd.\n')
        while True:
            switchtoNewMenu=input('do you want to create a new character? y=yes, n=no : ')
            if switchtoNewMenu=="y":
                New("\nCreate your first Character")

            elif switchtoNewMenu == "n":
                while True:
                    print("\nDo you want go back to Mainmenu ?")
                    switchtoMainmenu=input('y=yes, n=no : ')
                    if switchtoMainmenu =="y":
                        MainMenu("Main Menu","Choose a number","New","Load","Exit")
                        break
                    elif switchtoMainmenu=="n":
                        print("\n\n!!! The Programm is closing !!!")
                        exit()     
    else:
        saveCharacters=pd.read_csv('charactersaves.csv')
        print(saveCharacters)


   