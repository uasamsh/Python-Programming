print("hello")
print('hello')

print('''
      Hello
      Evryone 
      ''')

# Arithmetics operators
print(2+3) # int plus hongay list concatenate hoga
print(3.5 -2.1) # float
a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
c=4; d=-6
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c%d)
print(c//d)
print(c**d)
print("#########################")
x = 15
y = 4
z = 5.5
print(x-z*4/y+3)  # DEMAS DIV,MUL, ADD, SUB,: PEMDAS : BODMAS


a = "codanics"
b= "Pakistan"
print(a+b)

a = [1,2,3] # list
b = [4,5,6]
print(a)
print(b)
print(a+b)  # concatenate list
c = [4,5,6]
print(a==b)
print(b==c)  # boolean

# comparison or conditional operators

x = 11

y = 3

z = 5.2

print(x>y and y<z)

print(x>y or y>z)




# Data types

x = 5
y = 5.0
z = "Hello"

a = [1,2,3] # list of int
b = (1,2,3)  # tuple of int
a_1 = ["mango", "Banana"] # list of str
c = {"name saima": "Height 6.0", "name Dilip": "Height 6.2"}

print(c)

# input program

name = input("Enter your name: ")
print("Hello", name,  ", How are you? ")

person_A_name = input("Plz Enter Your Name: ")
person_A_age = person_A_name = input("Plz Enter Your age: ")

person_B_name = input("Plz Enter Your Name: ")
person_B_age = person_A_name = input("Plz Enter Your age: ")

if person_A_age > person_B_age:
  print(person_A_name, "Is Older than", person_B_name )
else :
    print(person_A_name, "Is Younger than  ", person_B_name )
name = input("Enter your name: ")
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight_kg / (height_m ** 2)

# Display the result
print(f"{name}, your BMI is {bmi:.2f}")