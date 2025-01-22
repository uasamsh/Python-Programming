# escape starts from backslash \
# After backslash \ one or more character can  write
#  escap sequane use for non pritntable character 
# represnt signle character
#  esc spaces are always builtin/iinbuilt or predefined
#  like backslash  "\n  means linefeed OR newline " means new line
print("Hello\nworld")
print(len("Hello world"))
print(type("Hello world"))
print(len("Hello\nworld"))  #  \n count single charachter not double
print(len("Hello\tworld"))  # \t used new tab

# ESCAPE MEANINGS
# \\BACKSLASH
#  \' SINGLE QUOTE (store ')
#  \" DOUBLE QUOTE (store ")
#  \a BELL   use in OS
#  \b BACKSPACE  Use OS
#  \f FORMFEED   use OS
#   \n NEWLINE     
#   \r CARRIAGE RETURN  use OS
#   \t HORIZONTAL TAB


# \\ double backslash  use , 1 is printable other is not printable
# if we wants output write this--> male\female
print("male\female") # cant write single bakslash use, output will be only male
print("male\\female") # now out put male\female for using \\ it means single backslash as printable

print("c:\new folder\text.txt") # cant write this type
print("c:\\new folder\\text.txt")  # right code 

#  \' SINGLE QUOTE (store ')
print('python program')
print('python\'s program') # with backslash comma
print("python's program")

#  \" DOUBLE QUOTE (store ")
print("python program")
print("python\'s program") # with backslash comma
print("python's program")

#  \a BELL  run through windows  isko use karnay se bell ya beep ki sound sunaye de ga, 
print("python\a program")

 #\b BACKSPACE
print("python\b program") # is main last  n overwite ho jaye ga p per
# \f FORMFEED   use for another platform
print("Hello\fworld") # output \f just symbol
#  \n NEWLINE  
print("Hello\nworld")

#   \r CARRIAGE RETURN   no run in python just worj on windows
print('python\r program')  # is main pehlay word ko dosara word overwrite kar de ga
# \t HORIZONTAL TAB
print("Hello\tworld")   # make 3 spaces
print('Name Ahmed:\t\tsalary: 500\t\tAge: 25\t\tphone number: 1212343243')
print('John\t\t800')

#  for perfect space each item OR list
print('name John\tsalary 500'.expandtabs(tabsize=15))
print('Nmae Ali\tsalary 800'.expandtabs(tabsize=15))




