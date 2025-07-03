import random


computer = random.choice([1,0,-1])
youstr=input("enter the choice:")
yourdict={"s": 1,"w": -1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you=yourdict[youstr]

print(f"you choice {reversedict[you]}\ncomputer choice is{reversedict[computer]}")

if(computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==1):
        print("you win!")

    elif(computer==-1 and you==0):
        print("you lose!")

    elif(computer==1 and you==-1):
        print("you lose!")

    elif(computer==1 and you==0):
        print("you win!")

    elif(computer==0 and you==-1):
        print("you win!")

    elif(computer==0 and you==1):
        print("you lose!")

    else:
        print("something wrong")        

   

