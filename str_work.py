

#str
#iterable
#seq



#name = "FARIBORZ"

#x=name.count("R")
#print(x)

"AZ-az1234567890+-*/!@#$%^&*()"

#a=65
#
#print(chr(a))
#i=0
#j=0
#for i in name:
#    i+=1
#    if "R" in name:
#        j+=1
#name = "FARIBORZR"   
#x=name.find("R",7,9)    
#print(x)

#for i in name:
#    print(i)




#name = "alireza"
#
#print(name[7:1:-1])

#name = "fariborz ekhtiari"

#x=name.endswith("ez")
#x=name.endswith("rz")
#print(x)

#x=name.index("r",0,8)
#print(x)


#x=name.title()
#print(x)
#name = "faRiborZ717171"
#name=name.upper()
#print(name)

#name=name.swapcase()
#print(name)

#name=name.strip()
#print(name)

#x=name.isalnum()
#print(x)
#name="fariborz"
#x=name.isalpha()
#print(x)
#name="fariborz"
#x=name.isascii()
#print(x)

#name="Fariborz"
#x=name.isidentifier()
#print(x)



user_pish="admin123"
password_pishfarz="admin123"

while True:
    main_menu=input("1.vorood 2.sabtenam 3.exit:") 
    while True:
        match main_menu:
            case "1":
                user_name=input("user:")
                pasword=input("password:")
                if user_name.isalnum()==True and pasword.isalnum()==True:
                    print("user va pass ok ")
                    
                
                if len(user_name)>8 and len(pasword)>8:
                    if user_name == "admin123" and pasword=="admin123":
                        print("login")
                        continue
                    if user_name != "admin123" and pasword!="admin123":
                        print("user ya pass eshteb .")
                        continue
                    
                    
            case "2":
                name=input("esm:").capitalize()
                family=input("famil:") .capitalize()   
                age=int(input("sen:"))
                if age>=18:
                    print("ok")
                else:
                    print("mojaz nistid.")
                    break
                
                email=input("email:") 
                if email.endswith("@gmail.com")==True:
                    print("email is ok ")
                else:
                    print("email mojaz nist.")
                    break
                
                adress=input("adress:")  
                if adress.isalnum()==True:
                    print("adress ok")  
                else:
                    print("adress ghabool nis")
                    break
                phone=input("phone:")
                if phone.startswith("09") or phone.startswith("0098") or  phone.startswith("+98"):
                    print("format mobile ok")
                if len(phone)==11 :
                    print("mobile shoma sabt shod")
                else:
                    break
                     
                pst=input("pst cod:")
                if pst.isnumeric()==True and len(pst)==10:
                    print("code pdt ok ")
                else:
                    print("pst ok nis")
                    break
                
                    
                    
                    
                
                 