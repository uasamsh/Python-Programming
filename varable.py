#  which one is good in both programs interactive program bcz anthything didnt work without user
#  Rigit programs are worst program
#  agar hum ko user se koi baat poochni hai to usko
#  variables/ refrence bhi kehtay hain ye user interactive program hoga
#  variavle is holde or container which store value which make in memory in c/c++, 
# But in python varible means name aik aisa naam jo kisi ko di gaya hai , means meray paas aik value hai usko aik naam de dia hai, yahan kabhi bhi var ka matlab box ya container nhn hai
#  python main reffrence ka kaam hota hai aur reffrence variable ke through banaye jatay hain
#  reffrence/variable are same in python but in c, c++ and java reffrence and variable are diffrent like:
#  int a;
# a = 5
#  if we write code 
# a = 5,76 then error bcz its not int , but in python:
#  a = 5   ye ban gaya isko hu data/litarls value/comst bhi bol saktay hain  python main 5 ka container nhn banta ...just c , c++, aur java main container bantay hain 

#  python main variable nhn hai reffrence hai lkn unko hi varibles kaha jata hai

#  python program access data through reffrence
# a = 2  # is ka matlab 2 store hua jisko naam di gaya hai a , 2 store in RAM


#  1) Store in memory
#  2)  a reffer this 2, a ke through 2 ko access kar saktay hain
a = 2 
b = a
print(id(a))
print(id(2)) # both output same id
print(id(b)) # 2 ki id a main aur a ki id b main 3no ki id same hogi, hum agar a ki value change kar den:
a = 5.6 # ab a ki value 2 nhn hogi 5.6 hogi id change hogi
print(id(5.6))
#  c c++ java main dabba bana ke value rakhtay hain python main aisay nhn hai is main vlue pehlay rakh di jati hai phir usko naam dia jata hai

# #  c c++ java main type batna parta hai int float char declare karna hota hai 
# int a = 5;
# float b = 5.7;
#  char c = "Ali";

#1) lkn python main type nhn batana parta is lie isko refference kaha jata hai variable nhn.
#  
#2) python prgram simple/easy banta hai
# 3) python nature dynamic hai kaisay?
# pehlay a ki value 4 thi phir a ki value 5.5 phir agar aik aur vale usekaren to overwrite kar ke ALI kar de gi , evironment ko change kar deta hai is lie isko dynamic programing kaha jata hai.
#  4)  python program flexible hai
#  5) easy to rea/write hai
#  6) type loose language
a = 4
a = 5.5
a = "Ali"
print(a)

e= 4 
f= 4
print(e+f) #  abhi ye program interactive nhn q k yahan pe value fix kar di hai user se input lenay ke lie
c= int(input())
d= int(input())
print(c+d) # run ke baad out put main koi 2 int value likh ke enter karen gay to woh sum hogi, is ko aisay bhi likh saktay hain 
print(" plz enter first number")
g = float(input())

print(" plz enter second number")
h= float(input())
print(g-h) # ab output main user float value put kar ke enter karay ga jo minus ho jaye gi

# @@@@@@@@@@@@

# vlue ko object bhi kah saktay hain, obect ka matlab hai ye indidually memory main ban gaya hai,  2 likha ya 2.0 likha to ye object ki memory ban jati hai , jo memory main ban jaye woh object se reffer ki ja sakti hai , 
# 2, 2.0, "2" Evrything is object

#  varibla ka naam identifier ho sakta hai keyword nhn ho sakta, 
#  make variable name we use alphabetic, number, _ underscor not use const start with number, ignore those name which starts from _ underscore, space is not allowed 

# alpha = 1   alpha is name jisko identifier kehtay hain
#  a = 2     a is name jisko identifier kehtay hain
#  varibles main naam/identifier hna chahiye lkn keyword nhn hona chahiye jaisay:
#  if = 23
# print (23) yahan pe if reserved keyword agar ye indentifier/naam den gay to error de ga, keyword use nhn krn variables/naam/ identifiers ke lie, lkn agar hum if ki jagah capital i ya F, If ya iF kar den to woh identifier ban jaye ga error nhn de ga.
#  camel case  , start from lower case like:fristNumber
#  Pascal case , start from capital case like: FirstNumber
#  snake case , just lower case with underscore like: number_of_clollege
# @@@@@@

#  in python a reffernce has no intrinsic type , ye kisi bhi type main convert ho jata hai like:

m = 9
print(type(m))

n = 9.89
print(type(n))

v = "HELlO WORLD"
print(type(v)) # m, n , v convert in all types so no intrinsic type

o = 3
p = 3
print(id(o))
print(id(p)) # dono ki id same output main hogi

o = 3
p = 3.7
print(id(o))
print(id(p)) # dono ki id different output main hogi

