#  7 types operators in pythons
# 1)Arithmatic operators 
#2) Assigmnent operators
#3) Comparison operators
#4) Logical operators
#5) Bitwise operators
#6)Identify operators
#7)Membership operators



#  operators are used to operations on variables and values
#  zruri nhn arithmatics opr hon kuch aisay bhi hotay hain jo numbers ke ilawa kisisi aur pe bh kam karaty hain

#  python main sab se choti cheez characters hotay hain jin se tokens banatay hain, Tokens kia hain 5 tokens hotay hain--> 1) keywords, 2) identifiers,
# 3)puctuators, 4)         , 5)literals 

#  punctuatores predefined hotay hain in main symbols aur brakets hotay hain

#  some oprators are uniary means 1, bianry at leat 2 value or operand 0\1, and turnery at leat 3 value or operand

# 1)Arithmatic operators
#  works on unary   means + plus  +2 is unary,  - minus -3 is binary ,  binary means + addition 2+ is binary, - subtraction 3- is binary agar + ya - pehlay aye to unary , agar +,- baad main aye to binary hota hai
#  They perform some methematics operators

#  unary

a = -4+5
print(a)
x= -4
y= 78
div= x / y

b= -4
print(b-4)  # yahan b ki jagah -4 aa gaya print main bhi -4 to result -8

print(div)
c = +-2
print(c)

d =   -(+(-6)) # - , - = +  and +,+ = +
print(d)

#  unary binary mix
e = 6+-8 # pehlay unary solve hota hai phir binary wala solve hota hai hamesha  (6) + (-8) = 6-8=-2
print(e)

f = 6+-+-3 #  (6)+(-(+(-3)))= 9
print(f)

a=2.3
b=3.3
c=a+-b
print(c)
print(type(c))

# binary
a = 4+5
print(a)
x= 4
y= 78
sum= x + y
print(sum)
#  OR
print(x-45)



print("$$$$$$$")
# print(x + 10)  work with value and reffrence\varible 

#  Multiplication * is binary,  *b pehlay ho to extend assignment, b* baad main aye to multiply

# extend opertor
a ,*b ,c = 1, 2, 3, 4, 5, 6
print(a)
print(b)
print(c)

# multiply is binary
w=3
r= 5
mul = 3*5
print(mul)

# division is binary operator
print("@@@@@@@@@@@@@@@@@@22")
a = 4/5
print(a)
print(type(a)) # result float main aye ga
x= 4
y= 78
div= x / y
print(div)

# Floor division // is bainary: agar ans c++ wala chahiye to iska use hota hai, ab result float main nhn int main hoga
a = 10//5
print(a)
print(type(a))

a=10.5
b=2.0
c=a//b
print(c)
print(type(c))

#  Eponentiation is binary  ** :  power of , 2 ki power 3 like:
a=2
b=3
c=a**b
print(c)
print(type(c))

a=2.3
b=3.3
c=a**b
print(c)
print(type(c))
print("!!!!!!!!!!!!!!!!")



# Remainder is binary 
a = 4%5
print(a)
x= 4
y= 78
mod= x % y
print(mod)

#  String  in ARithmatics operators
#  String arithmetics  ke sath binary opertaion allow hain unary nhn inko minus aur 
a="HI"
b="Hello"
c=a + b
print(c)
print(type(c))
#  String digits ke sath  ke sath multiply  kar saktay
a="HI"
b="john"
c=a * 3, 
print(c)
print(type(c))
a="Hello"
b="frndz"
c=a * 3, b * 2
print(c)
print(type(c))