#  Variants of data types 
#  2 types of data types
#  User-defined data types
# inbuilt/core data types/predefined data types int, float, complex,string, boolean, none, undefined, array, frozenset,list, set, tuple, dic, file, function, nonetype, classes, bytes, bytes array, memoryview

#  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#  data types means operation banana
#  operation in python program hinges on the data it handles.
#  data values are called object or value OR called date types
#  An object's type determine which operations the object supports(on ther word which operations you can perform the value) means us object pe kia kia operations laga saktay hain
print("*******************")

# type()  and isintance() ye dono functions hain aur built-in functions hain

# type() The built-in type(obj) accepts any object its arguments and return type object that is the type of obj.

h = "hello" # h reffernce karay ga hello ko
j = 3
k= 3.3
j= True
print(type(h))
print(type(j))
print(type(k))
print(type(j))


print(type(5))
print("hello" + "hi") # string

print(3+4)
print(3+3j) # complex number as it is print

# isintance() : is main 2 parameters hotay hain pehla object jiska type check karna hai dosara type check kartay hain means obj ka jo type hai woh given type ke equlent hai ya nhn hai, pehlay obj ka type nikalay ga phir type se match karay ga agar amtch hoye dono to True AGar same nhn hain to  False.
# The built-in function isintance(obj, type) return type True when object obj had type (or any subclass thereof); it return False 

g = 6
print(isinstance(g,int))
print(isinstance(g,str))

#  &&&&&&&&&&&&&&&&&&&&

# python types are determined automatically at runtime, not in response to declarations in your code.
#  python is given dynamic typed like:
v = "hello" 
v= 3
v= 3.3
print(type(v)) # change the value same refference make it dynamic

# @@@@@@@@

# Type casting: 
# Type casting some inbuilt fuction int, float, st, bool and more, 
# Type casting can change value
#  Type casting can generate error like: 
# b = int("hello")
#  print(b)
# print(type(b)) generate error bcz int str cant covrt in int but int convert in str
z = str(123)
print(z)
print(type(z))

z = bool(123) # jitnay bhi + aur - number hain true hain 0 false hai
print(z)
print(type(z))

z = bool(-12367.9) # True
print(z)
print(type(z))

z = bool(0)
print(z)
print(type(z))

z = bool("hello") # True
print(z)
print(type(z))

z = bool("") # false
print(z)
print(type(z))
print("############") 
b = float(1256)  # didnt gerate error
print(b)
print(type(b))

#  means float value change convert into int 
# aik typr ko dosari type ya aik obj ko dosari obj main convert karna like:
print("&&&&&&&&&&&&&&&&&")
p = int(6.89)
print(type(p))
print(p)   # .89 ko chor de ga ye type casting hai

