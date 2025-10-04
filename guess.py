import random


number = random.randint (1,100)
print ("Begin!!")
done = False
while (done == False):
    guess = int (input ("enter a guess: "))
    if guess == number :
        print ("You Guesed it !")
        done = True
    elif guess > number:
        print ("You're too high!")
        50
    else:
        print ("You're too low")
