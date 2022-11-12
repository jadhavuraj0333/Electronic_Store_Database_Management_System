import mysql.connector as mq

mysql = mq.connect(host = "localhost", username = "root", password = "root", database = "electronic_store")
if (mysql):
    print("Connection Establised")
else:
    print("Some Error")

cursor = mysql.cursor()


a = "WELCOME TO ELECTRONIC STORE"
print(a.center(50,"*"))

while 1:
    products = int(input("We sell all these products ::\n\t 1.Laptop \n\t 2.Mobile Phones \n\t 3.TV \n\nEnter an product's option that you want to buy : "))
    if (products == 1):
        title = "Laptop"
        print(title.center(40,"*"))
        laptops = int(input("Welcome to Laptops, we have these brands ::\n\t 1.HP \n\t 2.Lenovo \n\t 3.Dell \n\t 4.MacBook \n\t 5.Samsung\nEnter an option to see the details of the product : "))
        if (laptops == 1):
            cursor.execute("select * from product_details where product_code = 101")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many HP Laptop you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 101")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break  
       

        if (laptops == 2):
            cursor.execute("select * from product_details where product_code = 102")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity= int(input("How many Lenovo Laptop you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 102")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity}  \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break  

    
        if (laptops == 3):
            cursor.execute("select * from product_details where product_code = 103")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many Dell Laptop you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 103")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break  
            
        if (laptops == 4):
            cursor.execute("select * from product_details where product_code = 104")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many MacBook you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 104")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break
                
        if (laptops == 5):
            cursor.execute("select * from product_details where product_code = 105")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many Samsung Laptop you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 105")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break

    if (products == 2):
        title = "Mobile Phones"
        print(title.center(40,"*"))
        mobiles = int(input("Welcome to Mobile Phones, we have these brands ::\n\t 1.MI \n\t 2.Oppo \n\t 3.Vivo \n\t 4.Samsung \n\t 5.Oneplus\nEnter an option to see the details of the product : "))
        if (mobiles == 1):
            cursor.execute("select * from product_details where product_code = 201")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many MI phones you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 201")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break
            
        if (mobiles == 2):
            cursor.execute("select * from product_details where product_code = 202")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many Oppo phones you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 202")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break
            
        if (mobiles == 3):
            cursor.execute("select * from product_details where product_code = 203")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many Vivo phones you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 203")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break
            
        if (mobiles == 4):
            cursor.execute("select * from product_details where product_code = 204")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many Samsung phones you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 204")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity } \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break
            
        if (mobiles == 5):
            cursor.execute("select * from product_details where product_code = 205")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many Oneplus phones you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 205")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break

    if (products == 3):
        title = "Television"
        print(title.center(40,"*"))
        tv = int(input("Welcome to TV's, we have these brands ::\n\t 1.LG \n\t 2.Sony \n\t 3.Samsung \n\t 4.Panasonic \n\t 5.MI\nEnter an option to see the details of the product : "))
        if (tv == 1):
            cursor.execute("select * from product_details where product_code = 301")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many LG TVs you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 301")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break
            
        if (tv == 2):
            cursor.execute("select * from product_details where product_code = 302")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many Sony TVs you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 302")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break
            
        if (tv == 3):
            cursor.execute("select * from product_details where product_code = 303")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many Samsung TV's you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 303")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break
            
        if (tv == 4):
            cursor.execute("select * from product_details where product_code = 304")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many Panasonic TV's you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 304")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break
            
        if (tv == 5):
            cursor.execute("select * from product_details where product_code = 305")
            data = []
            for i in cursor:
                data.append(i)
            print(f"Product Code :: {data[0][0]} \nProduct Type :: {data[0][1]} \nProduct Brand :: {data[0][2]} \nProduct Price :: {data[0][3]}")
            quantity = int(input("How many MI TV's you want to buy ::  "))
            cursor.execute("select product_price from product_details where product_code = 305")
            price = []
            for i in cursor:
                price.append(i)
            a = price[0][0]
            print(f"Your total bill is --> \n\t Type :: {data[0][1]} \n\t Brand :: {data[0][2]} \n\t Price :: {data[0][3]} \n\t Quantity :: {quantity} \n\t Total :: {quantity} x {a} = {a*quantity}")
            x = input("Do you wish to buy anything else :: ")
            if (x.lower() == "no"):
                 print("Thank you for shopping..Visit again :)")
                 break

a = ("..THANK YOU..")
print(a.center(50,"*"))






