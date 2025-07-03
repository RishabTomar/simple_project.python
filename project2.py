from random import randint
n=randint(1,100)
a=0
guesses = 1
while(a!=n):
    a=int(input("guess the number:"))
    if(a>n):
        print("lower number please")
    elif(a<n):
        print("higher number please")
        guesses +=1
print(f"you have guessed the number {n} correctly in {guesses} attempts")            