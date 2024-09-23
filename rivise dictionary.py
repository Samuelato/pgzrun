dictie={}
while True:
    print(" 1. insert \n 2. display all sports\n 3. display all equipments\n 4. get equipments \n 5. delete ")
    userinput=int(input("1,2,3,4,5 what do you pick"))
    if userinput==1:
        varsp=input("enter sports:")
        equ=input("enter equipment:")
        dictie[varsp]=equ
    elif userinput==2:
        print(dictie.keys())
    elif userinput==3:
        print(dictie.values())   
    elif userinput==4:
        spor=input("enter the sport:") 
        print(dictie[spor])
    elif userinput==5:
        dele=input("wat do you want to delete please:")
        del(dictie[dele])
        print(dictie)