import random

x=random.randint(1,100)
print("play our gess the number game")
while(True):
    y=int(input("enter the number you guessed : "))
    if(x==y):
        print(f"you got it , the answer is {y}")
    elif(x>y):
        print(f"HINT : it is greater than  your guess {y}")
    else:
        print(f"HINT : it is smalller than your guess {y}")
