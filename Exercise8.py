userName = input("username : ")
passWord = input("password : ")
if userName == "phawinee" and passWord == "45574":
    print("---Welcome to Fruitshop---")
    print("1.apple   : 20 (THB)")
    print("2.coconut : 65 (THB)")
    print("3.banana  : 10 (THB)")
    print("4.cherry  : 55 (THB)")
    print("5.grape   : 30 (THB)")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = 20
        amount = int(input("Amount :"))
        result = (price * amount)
        print("Total",result,("THB"))
    elif userSelected == 2:
        price = 65
        amount = int(input("Amount :"))
        result = (price * amount)
        print("Total",result,("THB"))
    elif userSelected == 3:
        price = 10
        amount = int(input("Amount :"))
        result = (price * amount)
        print("Total",result,("THB"))
    elif userSelected == 4:
        price2 = 55
        amount = int(input("Amount :"))
        result = (price2 * amount)
        print("Total",result,("THB"))
    elif userSelected == 5:
        price2 = 30
        amount = int(input("Amount :"))
        result = (price2 * amount)
        print("Total",result,("THB"))
    else:
        print(userSelected,"don't have")
else:
    print("Invalid username or password")

