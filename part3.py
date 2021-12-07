'''
______
PART 3
______
Write a program that asks the user to input one integer. The program will then print two strings, one stating if it's positive, negative, or zero, and another that states whether or not is is divisible by 3. (Hint: to check divisibility by 3, you will find using the modulus(%) operation very helpful.)

3 examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a number:  -2
negative
not divisible by 3

Enter a number:  0
zero
divisible by 3

Enter a number:  5
positive
not divisible by 3
'''

#write your code below
num1 = int(input("Enter a number: "))

if num1 > 0:
  print("positive")

if num1 < 0:
  print("negative")

if num1 == 0:
  print("zero")

if num1 % 3 == 0:
  print("divisble by 3")
else:
  print("not divisble by 3")


num2 = int(input("Enter another number: "))

if num2 > 0:
  print("positive")

if num2 < 0:
  print("negative")

if num2 == 0:
  print("zero")

if num2 % 3 == 0:
  print("divisble by 3")
else:
  print("not divisble by 3")

num3 = int(input("Enter another number: "))

if num3 > 0:
  print("positive")

if num3 < 0:
  print("negative")

if num3 == 0:
  print("zero")

if num3 % 3 == 0:
  print("divisble by 3")
else:
  print("not divisble by 3")

num4 = int(input("Enter another number: "))
if num4 > 0:
  print("positive")

if num4 < 0:
  print("negative")

if num4 == 0:
  print("zero")

if num4 % 3 == 0:
  print("divisble by 3")
else:
  print("not divisble by 3")