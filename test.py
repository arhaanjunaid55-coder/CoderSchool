# DONE: Grab input from user
#DONE:input is >= 0 add 1 to input and mutiply by 4 and print the result
#DONEf input is < 0 then subtract 3 and multiply by 9 and print the result
#DONElse input is 0 then print out 0

def branchingPracticeFunc1 ():
    s = int(input("Enter a number: "))

    if (s > 0):
        print(s + 1 * 4)
    elif (s < 0):
        print(s - 3 * 9)
    else:
        print(s)

def branchingFunc2 ():
    x = int(input("Enter a number x: "))
    y= int(input("Enter a number y: "))

    if ( x > y ):
        print("X is greater than Y")
    elif (y > x):
        print("y is greater than x")
    else:
        print("X and y are equal")

# grab input from user into variable x
# grab input from user into variable y
# if x > y print "x is greater than y"
# if y > x print "y is greater than x"
# if x = y print "x and y are equal"

# grab input form user into a variable called max
# grab input form user into a second variable called min

# make max be the gratest of the 2 numbers
# and min be the smalles of the 2 numbers

max = int(input("enter a number for max: "))
min=int(input("enter a number for min: "))

if (max < min):
    print ("max: ", max, " min: ", min)
    temp = max
    max = min
    min = temp
    print ("max: ", max, " min: ", min)
