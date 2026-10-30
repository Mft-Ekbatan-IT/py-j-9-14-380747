



from factor import *


while True:
    menu_cafe=input("1.CAKE       2.COOFFEE       3.EXIT :")
    while True:
        match menu_cafe:
            case"1":


                menu_cake=input("1.Rolet        2.Nuttla 1500          3.Vanil 1200 :")
                match menu_cake:
                    case"1":
                        gheymate_rolet= int(input("malagh rolet:"))   
                        tedad_Rolet=int(input(" chan ta mikhoy :"))
                        resid(tedad_Rolet,gheymate_rolet)

                    case"2":

                        tedad_Nutella=int(input(" chan ta mikhoy :"))
                        gheymat_Nutella=tedad_Nutella * 1500 * 1.1
                        print(gheymat_Nutella)

                    case"3":

                        tedad_Vanil=int(input(" chan ta mikhoy :"))
                        gheymat_Vanil=tedad_Vanil * 1200 * 1.1
                        print(gheymat_Vanil)
                            
                        factor.append(tedad_Rolet)
                        factor.append(tedad_Nutella)
                        factor.append(tedad_Vanil)
                break
            case"2":

                menu_cooffee=input("1.Americano  250           2.Esperco  200        Late  300 :")
                match menu_cooffee:
                    case"1":

                        tedad_Americano=int(input(" chan ta mikhoy :"))
                        gheymat_Americano=tedad_Americano * 250 * 1.1
                        print(gheymat_Americano)

                    case"2":

                        tedad_Esperco=int(input(" chan ta mikhoy :"))
                        gheymat_Esperco=tedad_Esperco * 200 * 1.1
                        print(gheymat_Esperco)

                    case"3":

                        tedad_Late=int(input(" chan ta mikhoy :"))
                        gheymat_Late=tedad_Late* 300 * 1.1
                        print(gheymat_Late)

                        factor.append(tedad_Late)
                        factor.append(tedad_Americano)
                        factor.append(tedad_Esperco)
                break
            case"3":
                break      
            
                            



                     