#    Nested for loop 
# using for multidimentional data
colors = ["red", "green", "blue"]
items = ["book", "pen", "copy"]

for color in colors:
    for item in items:
        print(color, item)

 # reverse       
colors = ["red", "green", "blue"]
items = ["book", "pen", "copy"]

for color in colors:
    for item in items:
        print( item,color)

# Nested While loop

i = 0
while i <3:
    j = 0
    while j < 3 :
        print(i,j)      
        j = j +1
    i = i+1  
print("@@@@@@@@@@@@@@@@")   
#for loop inside while loop
x=5
while x < 10:
 
    for y in range(20):
        print(x,y)
    x += 1
print("###################") 
# while loop inside for loop
x=0
for y in range(10):
   while x < 5:
        print(x,y)
        x = x+ 1