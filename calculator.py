
#from random import choice


num1 = float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))
 
print("Calculator")
print("1 for addition")
print("2 for subtraction")
print("3 for Multiplication")
print("4 for Division")

choice= int(input(" Enter choice from 1,2,3,4 : "))



if choice == 1:
       print(num1+num2)

elif choice == 2:
       print(num1-num2)
elif choice == 3:
       print(num1*num2)

elif choice == 4:
       print(num1/num2)
else:
     print(" Invalid number Please Enter Number From 1,2,3,4")




