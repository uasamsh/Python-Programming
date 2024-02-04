
# Strings are immutable

a = "UZma"
print(len(a))

print(a.upper())
print(a.lower())

b =" !!!!!!!! Shah Syed !!!!!!!!!"

print(b.strip("!"))

print(b.replace("Syed","Ahmed"))

# using list in string use split method

c = "Syed"
print(c.split(" "))


# using in capitalize
blogheading = "introduction to python jS"

print(blogheading.title())

# using just 1st letter capitalize
print(blogheading.capitalize())


str1 = "Welcome to the Console!!!"
print("##########")
print(str1.endswith("!!!"))

print(str1.endswith("to", 4, 10))

print(str1.startswith("U"))

print(str1.title())

print(str1.swapcase())

print(len(str1))

print(str1.center(50))

print(str1.count("a"))

print(str1.count("a",0,10))

u = "Shah Shah"
print(u.count("Uzma"))

# use to find index
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
# give  -1 if string not found
print(str1.find("ishhh"))

print(str1.index("an"))

# isalnum alpha numeric
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

#\n is not ptintable
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

# swaping capital words
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())




