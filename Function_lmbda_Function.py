# A function is a block of code which only runs when it is called
# you can pass data as an known parameter into a fuction
# Function can return data as a result
#  in python , a function can define as def keyword

def greet_person():
    print("Hello")
greet_person()   # calling the function

def aoa():
    print('AOA How r u?')
aoa()    

def person(name):
    print(f"Are you {name}? Hi how r u ?")
person("John")

#  by default 

def person(name = "Ammar"):
    print(f"Are you {name}? Hi how r u ?")
person()

# Return values

def square(number):
    return number * number
print (square(5))

def factorial(n):
    if n ==1:
        return 1;
    return n*factorial(n-1)
print ("Factorial of ",3,"is",factorial(4)); # 4*3*2*1=24
    
print("@@@@@@@@@@@@@@@@@")
def x (a):
    return a/2    
print(x(80))

# Function with  parameters and 
def hello_world(name):
 print(f"Hi How r u ? {name}")
hello_world("Ammar")


# lambda function means code write in one line

x = lambda a : a +10
print(x(20))

x = lambda a,b: a*b
print(x(20,5))


x = lambda a,b: a/b
print(x(40,2))


