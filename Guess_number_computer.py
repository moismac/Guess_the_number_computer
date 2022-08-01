from ast import Return
import random
"""
goal = 6
computer = random.randint(0, 10)
def Guess_number_computer (goal, computer):
    if goal < computer:
        print (f"Try agin!, number {computer} incorrect is greater than the goal")
        computer = Guess_number_computer(0, random.randint(0, computer-1))
        
    elif goal > computer:
        print (f"Try agin!, number {computer} incorrect is lesser than the goal")
        computer = Guess_number_computer(10, random.randint(computer+1, 10))
    elif goal == computer:
        print(f"Congratulation!, the number {computer} was the correct")
Return 
Guess_number_computer(goal, computer)
"""


def Guess_the_number(x):
    print (f"Insert a number between 1 y {x}")
    min_limit = 1
    max_limit = x
    anwser = 0
    while anwser != "c":
        #Generate a prediction
        if min_limit != max_limit:
            prediction = random.randint(min_limit, max_limit)
            print(min_limit, max_limit)
        else:
            prediction = min_limit
        
        anwser = input (f"Mi prediction es {prediction} Si el valor {prediction} es alto ingrese (a) si es bajo ingrese (b)y si coincide igrese (c): ").lower()
        
        if anwser == "a":
            min_limit = prediction - 1
            print( min_limit, max_limit)
        elif anwser == "b":
            min_limit = prediction + 1
            print(min_limit)
    print(f"Congratulation!, the computer guess your number: {x}")


Guess_the_number(10)