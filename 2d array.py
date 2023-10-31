from tkinter import END


list = [["1","2","3","4","5"],["6","7","8","9","10"]]

for x in list:
    for i in x:
        print(i)

choose = int(input("Would you like to append or remove something? [1 for append, 2 for remove]: " ))
if choose == 1:
    append = str(input("What would you like to add on?: "))
    list.append[(append)]
if choose == 2:
    delete = str(input("What would you like to delete?: "))
    list.remove[(delete)]
else:
    quit = str(input("Invalid selection, would you like to quit? (y/n):"))
    if quit == "y":
        print("ok")
        END
    if quit == "n":
        print("too bad")
        END
    if quit != "y" and quit != "n":
        print("STOP MAKINF THINGS HARDER")
        END