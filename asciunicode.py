# esc squence ka representation
#  \n called normal form, linefeed, newline, single character
#  ye dekhna hai is number ka Asci ya Unicode kia hai us ke lie ordinal ord use hota hai
#  A ke peechay unicode ka number kia hai 
print(ord("A"))

#  hamaray paas aik character hai us ke peechay decimal laga hai ye jananay ke lie ord lagayen gay
print(ord("\n"))
print(ord("a"))
print(ord("@"))
print(ord("%"))
print(ord("z"))
print(ord("*"))
print(ord("&"))

# agar decmal hai us ke peechay kia character laga hai us ke lie chr
print(chr(65))
print(chr(64))
print(chr(97))

#  \n covert decimal octa hexa
#  pehlay \n ka decimal nikaltay hain
print(ord("\n"))

#  ab is \n  ka octal nikaltay hain
print(oct(ord("\n"))) 

#  ab is \n  ka hexa nikaltay hain
print(hex(ord("\n"))) 
#  \n ka    decmal code      octal code     hexadecimal code
#   \n        10                0o12           0xa    ye kaisay ata 

# \n use
print("foldr\nnewcar")

# \012 use
print("foldr\012newcar")
#  \x0a use
print("foldr\x0anewcar")


#  kisi bhi escape squence ko 3 form main use kar saktay hain
#  aik normal form\n, dosari octal form aur 3sari hexa form main bhi dikha saktay hain  ziada better \n hi rehta hai

#  google   utf-8character with hexa   jo pehli list aye google main usko open karna hai

#  isko aisay bhi kar saktay \t ka hexa dekhnay ke lie jo out aye ga uska use

print(hex(ord("\t")))

#  \t output x09, then use it hexa main likhnay ke lie
print("forlder\x09newcar")


#  pak ruppe sign
# print("Shaan\t \N{ INDIAN RUPEE SIGN} 500")
# print("Shaan\t \N{US DOLLAR SIGN} 500")