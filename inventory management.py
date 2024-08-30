import os
os.system
import json
products={"Dal":7,"Moong":12.25,"Chilly Powder":22 ,"Turmeric Powder":20,"Coriander Powder":20.50,
          "Caraway seed":42,"Mustard":15,"Cumin seed":35,"Coriander seed":30,"Cardamom":180,"Cinnamon stick":25,
          "Cinnamon powder":42,"Fenugreek seed":20,"Pepper":70,"Clove":65,"Carrot":5.95,"Cucumber":4.95,"Tomato":4.75,
          "Coconut":2.75,"Potato":2.50,"Brinjal":6.95,"Apple":8.95,"Mango":16,"Grapes":17.95,"Watermelon":2.95,
          "Pineapple":5.25,"Stawberry":14.50,"Blackberry":14.50,"Kiwi":14.95,"Dragon fruit":17.95,"Orange":15}
staff={"Aditya":{"salary":2500,"designation":"Saleman"},"Arya":{"salary":3000,"designation":"Cashier"},"Adul":{"salary":2500,"designation":"Salesman"},"Aadira":{"salary":3000,"designation":"Cashier"},"Baneet":{"salary":3000,"designation":"Customer Service"},
       "Caterine":{"salary":6000,"designation":"Manager"},"Dennis":{"salary":5500,"designation":"Maintanence Supervisor"},"Erwin":{"salary":3000,"designation":"Maintanence technician"},"Grace":{"salary":3000,"designation":"Cashier"},"Jesica":{"salary":3000,"designation":"Customer Service"},
       "Jerik":{"salary":2000,"designation":"Cleaner"},"Jeffin":{"salary":6000,"designation":"PRO"},"James":{"salary":2000,"designation":"Cleaner"},"Joe":{"salary":3000,"designation":"Maintanence Technician"},
       "Haritha":{"salary":2000,"designation":"Cleaner"},"Harsh":{"salary":3000,"designation":"Maintainence Technician"},"Haris":{"salary":3000,"designation":"Maintanence Technician"},"Hamad":{"salary":5500,"designation":"Maintanence Supervisor"},
       "Imran":{"salary":3000,"designation":"Maintanence Technician"},"Irfaan":{"salary":2500,"designation":"Saleman"},"Isha":{"salary":2500,"designation":"Salesman"},"Ishan":{"salary":5000,"designation":"Supervisor"},
       "Kevin":{"salary":5000,"designation":"Supervisor"}}
print()
print()
print("------------Welcome To Veggies Supermarket------------")
print()
print("Enter 'C' if you are a customer")
print("Enter 'S' if you are a staff")
print()
D=input("Enter your choice(C/S):")
if D=="C"or D=="c":
    while True:
        print("1.To know the price of the product")
        print("2.To Buy")
        print("3.To exit")
        print()
        ch=int(input("Enter your choice(1,2,3):"))
        if ch==1:
            pro=products.keys()
            for i in pro:
                print(i)
            p=input("Enter the product name whose price is to be known")
            if p not in products.keys():
                print(p,"not available")
            else:
                price=products[p]
                print("Price of",p,"is",price,"Dhs")
            
        if ch==2:
            prod=products.keys()
            for i in prod:
                print(i)
            sum=0
            while True:
                print("Enter 1 to enter products to be Purchased")
                print("Enter 2 to exit")
                print()
                cho=int(input("Enter your choice(1,2):"))
                if cho==1:
                    buy=input("Enter product name:")
                    if buy in products:
                        sum+=products[buy]
                    else:
                        print(buy,"not available")
                if cho==2:
                    print()
                    print("Total sum:",sum,"Dhs")
                    print("Thank you for shopping!!!")
                    break
        if ch==3:
            break
if D=="S" or D=="s":
    pww=str(input("Enter password:"))
    if pww=='1a2b3':
        while True:
            print("1.To change price of a product")
            print("2.to enter a new product")
            print("3.to delete a product")
            print("4.To know all staff details")
            print("5.To know a particular staff detail")
            print("6.To change staff salary")
            print("7.To change staff designtion")
            print("8.To remove a staff")
            print("9.To add a staff")
            print("10.To exit")
            print()
            ch=int(input("Enter your choice:"))
            if ch==1:
                print("Prices of products")
                for v in products:
                    print(v,":",products[v])
                p=input("Enter product name who's price is to be changed=")
                if p in products:
                    z=float(input("Enter new price:"))
                    products[p]=z
                    print()
                    print(p,"=",products[p],"Dhs")
                else:
                    print("product not available")
            if ch==2:
                np=str(input("Enter new product name="))
                pr=float(input("Enter price of the product:"))
                products[np]=pr
                print(json.dumps(products,indent=3))
            if ch==3:
                dp=input("Enter product name which is to be deleted:")
                if dp in products:
                    del products[dp]
                    print(json.dumps(products,indent=3))
                else:
                    print(dp,"not available")
            if ch==4:
                print(json.dumps(staff,indent=2))
            if ch==5:
                i=input("Enter name of the staff:")
                if i in staff:
                    print("staff name:",i,"staff salary:",staff[i]['salary'],"Dhs","staff designation:",staff[i]['designation'])
                else:
                    print(i,"not a staff")
            if ch==6:
                name=input("Enter staff name")
                if name in staff:
                    nsal=int(input("Enter new salary"))
                    staff[name]['salary']=nsal
                    print("Staff name:",name,"staff salary:",staff[name]['salary'],"Dhs")
                else:
                    print(name,"not a staff")
            if ch==7:
                name=input("Enter staff name")
                if name in staff:
                    nd=input("Enter new designation")
                    staff[name]['designation']=nd
                    print("Staff name:",name,", staff designation:",staff[name]['designation'])
                else:
                    print(name,"not a staff")
            if ch==8:
                name=input("Enter staff name who is to be removed")
                if name in staff:
                    del staff[name]
                    print(json.dumps(staff,indent=3))
                else:
                    print(name,"not a staff")
            if ch==9:
                name=input("Enter name of the new staff:")
                sal=int(input("Enter salary:"))
                desi=input("Enter designation:")
                staff[name]={'salary':sal,"designation":desi}
                print("Staff name:",name,"Staff salary:",staff[name]['salary'],"Dhs","Staff designation:",staff[name]['designation'])
                print(json.dumps(staff,indent=3))
            if ch==10:
                break
    else:
        print("Entered wrong password")

