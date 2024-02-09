
""" 
The chr function asks for a parameter and an integer value should be passed in this function. The character value is also calculated according to that value.

While the ord function is a total reverse case of the chr function, when a string is passed through ord function, it returns the number.

The chr() function takes an integer and converts it to a character, so it returns a character string. The ord() function takes a single Unicode character and returns an integer value."""

# conver Ascii Unicode Character A to 65
a= 67
print(chr(a))

b = "A"
print(ord(b))

c = "H"
print(ord(c))
# other method
x = (65)
print((x))

x = chr(65)
print(type(x),x)

y = ord("B")
print((y))

x = ord("C") # Capital c
print(type(x),x)
x = ord("c") # small letter c
print(type(x),x)