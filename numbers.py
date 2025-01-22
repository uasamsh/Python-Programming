# wscube Tech video part 1 link-->   https://www.youtube.com/watch?v=xpWYAfl9pJE
# There are 5 types tokens available

# 1) keyword    reseved keyword constant

# 2)Identifires name number  constant

# 3) Punctuators are 2 tyoes operators + ,- ,<,>, =,and delimetres {},(),[]

# 4)whitespaces \t  tab, space, Enter, indent

# 5) literals are called value data or contanat there are exist 4 literals which are:
#  numbers, boolean , none, string


# 1) NUMBERS:
# python have 3 types of numbers 

# integer number,     float ya floating point number  , complex number are real number image number
# 2, -3 , +4,          6.07, -7.890, 34.67               3+ 4j ,  0+3j,   2j

# In literals number there are 3 types INTEGER , FLOATING, COMPLEX NUMBERS
# No. 1 is  int literals number
print(2)
print(type(2))
print(2+3)
 
#  No. 2 is FLOATING  1st METHOD floating number with normal form
print(.5)
print(type(.5))
print(3.5 +6)
print(type(3.5+6))
print(-3.5 +6)

#  2nd METHOD FLOATING LITERALS NUMBERS we can write floting number/ fraction number with e called exponencial form OR Scientific Form, 2e2 it means 2 power of 2  ...  2 * 10 * 10 = 200 ,
print(2e2)
print(type(2e2))
#  2 power of -03 ... 2x -10x -10x-10
print(2e-03)
#  5 power of 3 means 5x10x10x10=
print(5e3)
#  200 power of 3  .... 200x10x10x10=200000    2 lakh
print(200e3)

# write in scientific form OR exponential form make short the value for write
print(10000000000)
print(1e10)

# NO 3 is COMPLEX literals number.... 2 types of complex number exist real part and imaginary part like 
# 3+4j or 3+4J write in capital also 3 is real part + 4j is imaginary part
print(3+4j)
print(type(3+4j))

# Boolean litalas TRUE FALSE are keywords
print(True)
print(False)
print(type(True))

a = True
print(True)

#  TRUE means 1 , FALSE means 0 ... when i write 2+TRUE output will be 3 bcz TRUE IS 1
print(2 + True)
print(2 + False)
print(2>3)
print(9<10)

#  NONE is also litarals it is also keyword ...  NAN means NOT A NUMBER is separate concept
#  sometimes we work on None keyword
print(None)
print(type(None))
a = None
print(a)

#  STRING means text constent or string constant for example  name , NIC, Acoount no., Age, aisa data jis main text aa raha ho wahan hmn handle karna hai string contant/text constant

#  Strings are 2 types single line string and double line string

#  string is a  collection /set of characters on which we use Alphabet "Hello", numbers "hi123" and symbols "hello@frnd", 

# "" UNDERSCORE  are NOT A PART OF STRING  they are just " opening string and closing string "

#  Acctual string is Hello not underscore "" This is just a fomat/notation.  

# It is slash | ,  foarward slash / work for division,  backward slash \,

# string is with double quotation 

#  Single line strimg
print("Hello World")

#  if we want in between string underscore " then we write with single quotation

print('Hello\' Friend')

#  if we dont use backward slash then we write with single quotation
print('Hello " FRND')
# OR
print("Hello ' FRND")

#  if we want output with double quotation "" then write

print("\" Hello \"")
print(' "Hello frndz" ')

#  double OR Multiple line strings

print(''' Hello
      frndz
      my name is
       SARA''')
# OR
print("""Hello
      frndz
      my name is
       JOHN """)

#  if we write in multiple lines and teake output in single line then
print('\
       hi\
      frnds\
      ')
# without spaces
print('\
hi\
 frnds\
')
#  we can use it for multiple line
print("Hello")
print("frnds")

#  for new line
print("Hello\nfrndz")
print("Hello\tfrndz")

# BACK SLASH program main multiple line string allow hain lkn output single line main de ga
# MULTIPLE LINES strings  program main multiple line string allow hain output bhi multiple line string de gi.... strings are in Python immutable means aik baar string bangaye to changes allow nhn hain
