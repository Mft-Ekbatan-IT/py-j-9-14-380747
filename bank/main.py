
from tarakoneshha import*
from varizi import *
from bardashtha import *
global balance
while True:
    menu = input("1.variz 2.bardasht 3.namayesh mojoodi 4.namayesh tarakonesh ha 5.majmoe variz ha 6.exit: ")
    
    match menu:
        case "1":
            amount = int(input("mablagh variz: "))
            variz(meghdar=amount)
            
        case "2":
            amount = float(input("mablagh bardasht: "))
            bardasht(bardashti=amount)
        case "3":
            print("mojoodi feli:", balance)
            
        case "4":
            tarakonesh()
            
        case "5":
            sum_variz = 0
            for t in transactions:
                if t.startswith("+"):
                    sum_variz += float(t[1:])
            print("majmo variz ha:", sum_variz)
            
        case "0":
            print("exit")
            break
            
        case _:
            print("gozine eshtebah!")
            # break