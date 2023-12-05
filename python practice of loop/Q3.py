from random import *
c_num = randrange (1,10)
U1 = input("User 1 : Enter your name : ")
U2 = input("User 2 : Enter ypur name : ")
score = 10
attempt = 10
while 1:
    y_num1 = int(input(f"Guess the number by {U1}"))
    if y_num1 == c_num :
        print("You Win with score :",score)   
        break
    elif y_num1> c_num:
        print("Too large with score :",score)
        print("Attempt left : ",attempt)
    else:
        print("Too small with score :",score)
        print("Attempt left : ",attempt)
    score = score - 1
    attempt = attempt - 1