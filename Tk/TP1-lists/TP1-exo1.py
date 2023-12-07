import random as rand
def randomNum():

    num = rand.randrange(100,1000)
    num = list(str(num))
    print("enter a number that contain 3 digits :")
    count =0
    print(num)
    while(count<10):
        ccmp = False
        user = list(str(input()))
        exist=0
        for i in range(3):
            if(user[i]==num[i]):
                print("CCBP")
                exist+=1
            elif(num[i] in user):
                print("CCMP")
        if(exist==0):
            print("ACC")
        
        elif(exist==3):
            print("tu as deviner le nombre correcte, veux tu continuer(Y/N)")
            confirmation = str(input())
            if(confirmation.upper()=="Y"):
                randomNum()
    print(num)
    return "i"
print(randomNum())
