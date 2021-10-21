#You can change Text at Inputs

num1 = float(input("Enter Firt Number:"))
num2 = float(input("Enter Second Number"))

result= 0
op = str(input("Enter an op(operator)"))
#Gets Input Type--------
try:
  #U can make this in while loop ;-)
  if op=="+":
    result = num1 + num2
  else if op=="-":
    result = num1 - num2
  else if op=="*":
    result = num1 * num2
  else if op=="/":
    result = num1 / num2
  else:
      print("Invalid Input")
  print("The result is " + result)
except ZeroDivisionError:
  print("U cant do that")
