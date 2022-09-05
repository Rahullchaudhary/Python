import random 
x=random.randint(1,100)
guess=1
a=int(input("enter a number b/w 1 to 100:"))
game=False
while not game:
    if(x==a):
        print(f"You win!!! and gussed this number in {guess} times")
        game=True
    else:        
        if(x>a):
            print("Too low:")
        else:
            print("Too high:")
        guess +=1
        a=int(input("guess again!:"))


