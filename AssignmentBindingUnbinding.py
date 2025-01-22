#  Binding UNbinding of reffrence
#  in python there is no declaration
#  a reffrence begins with the statement that binds the reffrence (in other words, sets a name to hold a reffrence to some object) a = 2 ... a --> 2 ko reffer kar raha hai isko binding kehtay hain
#  del statement lagayen gay to woh unbind ho jaye ga



#  Assignment statement use to bind a reffernce to an object\vlaue \data\constant
#  Assignment statement =  are most common way in binding like : a = 2 iska mtalab 2 value ko a reffer kar raha hai
#  pehli baar likhen gay to bind like a =2 , dasari baar likhen gay to usko rebind boltay hain a = 3.4


x = 2      # binding
print(x)
x = 3.4    # rebinding
print(x)

#  now delete it 

del x    # unbinding ab a ki value delete ho gaye to ab print karen gay to 
 
# print(x)    # error de ga print nhn hoga q k a ki value delete ho gaye hai yani ke hum ne unbind kar dia hai ab hum isko binding kar saktay alag statment ke sath

x = " hello" # again binding with existing reffrence
print(x)

a = 2,3
print(a)   # result in tuple

# ***************


#  Assignment statement 2 methods: 1) plain Assignment, 2) Augumented Assignment 
#  1) plain Assignment  = ,  variable = value|expression, The value is s =2  and The Expression are s = 2+3+4
r =2 # value
print(r)

s = 2+3+4 # Expression 
print(s)

# in plan assignment we can write multiple ssignments like:  a=b=c=2 -->  it means c main aa gaya 2 , phir 2 b main phir main to pehlay c reffer karay ga 2 ko phir b aur phir a like:

d=e=f=2 
print(d)
print(e)
print(f) # in 3no ne reffer kia 2 ko

d=e=f=2 
print(id(d))
print(id(e))
print(id(f)) # same id


#  Extebded UNpacking:  two or more with separate comma like: a,b,c =3 ye error de ga,  a,b,c = 4,5,6,  ye error nhn de ga like:
#  r, s, t= 1,2,3,4,5,6   ye error de ga to hum * ka use karen gay l  ike:
print("Extebded UNpacking")
g,h,i = 4,5,6,
print(g,h,i )# OR seoarate we can write both
print(g)
print(h)
print(i)

#  agar r, s, t= 1,2,3,4,5,6 hai to us ke lie s ke sath * lagay ga like: r, *s, t= 1,2,3,4,5,6  aisay main r reffer karay ga 1 ko t reffer karay ga 6 ko ab s reffer karay mid vlues ko 2,3,4,5
print("Extebded UNpacking")
r, *s, t= 1,2,3,4,5,6
print(r)   # r ko 1 assign hoga
print(s)    # s ko 2,3,4,5 asign hoga aur list bana de ga
print(t)    # t ko 6 assign hoga

*r, s, t= 1,2,3,4,5,6
print(r)   # r ko 1,2,3,4 assign hoga list
print(s)    # s ko 5 asign hoga aur list bana de ga
print(t)    # t ko 6 assign hoga


print("NOW")
r, s, *t= 1,2,3,4,5,6
print(r)   # r ko 1 assign hoga list
print(s)    # s ko 2 asign hoga aur list bana de ga
print(t)    # t ko 3,4,5,6 assign hoga

#  sawping

x=4
y=6
print("Before Swaping")
print(x)
print(y)

x=y, y,x  
print("After Swaping")
print(x) 
print(y)

# *************************

#  2) Augumented Assignment/operators  or called in-place assignment  are :
# +=, -=, *=, /=, //=, %=. **=, |=, >>=, <<=, &=,^=, @=.
# only one target or reffrence LHS Aygments dost support multiple target on LHS
print("Augumented Assignment/operators ")
n = 2
print(id(n))
n += 3  # n = n+3 = 5 output
print(id(n))   #diiferent id both have

n = 2
n /= 3  
print(n)

n = 2
n **= 3  
print(n)

n = 2
n >>= 3  
print(n)

n = 2
n <<= 3  
print(n)

n = 2
n &= 3  # n = n+3 = 5 output
print(n)

n = 2
n |= 3  # n = n+3 = 5 output
print(n)



