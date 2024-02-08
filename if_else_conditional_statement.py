
a = input("Enter Your name : ")
print("Hello " + a)

b= int(input("Enter Your age : "))
print("Your age is : ", b)

if (b<12):
    print("You are kid")
elif(b<=18):
    print("you are a young")
elif(b<40):
    print("you are Adult")
elif(b>50):
    print("you are old")
else:
    print("invalid Age")

n = int(input("ENter the  number  from user : "))
if n < 0:
    print(" The number is negative")

elif(n ==0):
    print("The number is zero")  
elif(n== 999):
   print("number is special") # if  you write output is -999 then it is special number
else:
    ("number is positive")



# other
numb = int(input("Enter a number : "))    

if numb % 2 == 0:
    print("number is even")
else :
    (" number is odd")    



# program budget
# c = int(input("Enter Your budget : "))
# d = int(input("Enter price of apple : " ))
budget = int(input("Enter Your budget: "))
apple_price = 30  # Assuming the price of an apple is fixed at 30
if budget >= apple_price:  # if buget geater than apple price then print it
    print( " alexa , ADD 1 KG APPLE TO THE CART")

else:
    print("invalid budget")


 
# Nested loop 
    
    num = 18
if num < 0:
    print("The number is negative")
elif(num > 0):
    if(num <=10):
        print("The number is Between 1-10")
    elif(num > 10 and num <=20): 
        print("The number is between 11 -20")
    else: 
        print("The number is above 20")
else:
    print("Invalid number")    


# another for user input number    

num = int(input("Enter a number : "))
if num < 0:
    print("The number is negative")
elif(num > 0):
    if(num <=10):
        print("The number is Between 1-10")
    elif(num > 10 and num <=20): 
        print("The number is between 11 -20")
    else: 
        print("The number is above 20")
else:
    print("Invalid number")            



