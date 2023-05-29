import Menus

#Main Menu
ChoosenNumber=Menus.MainMenu("Main Menu","Choose a number","New","Load","Exit")
if ChoosenNumber==1:
       NewMenuNumber=Menus.New("Create New Character")
elif ChoosenNumber==2:
    LoadMenuNumber=Menus.Load("Character Overview")
elif ChoosenNumber==3:
    exit()
