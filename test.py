# DONE: Grab input from user
#DONE:input is >= 0 add 1 to input and mutiply by 4 and print the result
#DONEf input is < 0 then subtract 3 and multiply by 9 and print the result
#DONElse input is 0 then print out 0

s = int(input("Enter a number: "))

if (s > 0):
  print(s + 1 * 4)
elif (s < 0):
  print(s - 3 * 9)
else:
  print(s)