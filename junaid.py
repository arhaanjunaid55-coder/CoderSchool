def calcualtor(a, b, op):
    if op == "+":
     return a + b
    elif op == "-":
      return a - b
    elif op == "*":
      return a * b
    elif op == "/":
      return a / b
    else:
      print("ERROR!")

    
    

a = int ( input ("variable A:" ))
b = int ( input ("variable B:"))
op = input ("operator:")
result = calcualtor (a,b,op)
print (result)