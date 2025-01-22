#    NUMBer SYSTEM CONVERISON
# wscube Tech video main 7 hours pe binary nikalnay ka easy method copy below link
# https://www.youtube.com/watch?v=xpWYAfl9pJE
#  NUMBer SYSTEM CONVERISON:
#  decimal , hexa or octal number first convert in binary and then convert in decimal hexa or octal

# coversion bin to decimal , decimal to bin... in decimal  number series in computer like this 
# 1, 2, 4, 8 , 16, 32, 64, 128, 256, 512, 1024....
#  conversion d2b means decimal to binary we  have 50 decimal covert in decimal 32+16+2= 50
# 1, 2, 4, 8 , 16, 32, 64, 128, 256, 512, 1024....
# 0   1  0  0   1   1                           Now 50 covert in bin = 010011 now b2d convert 100011
# 1   0  0  0   1   1                           count 1 values          now decimal number is= 49

# 1st method B2D BIN 1001 CONVERT IN DECIMAL       1001 base 2
#          1                           0                      0                     1           base 10
#   2 power of 3 = 8          2 power of 2 = 4            2 power of 1 = 2     2 power of 0 = 1
#     8 x 1 = 8                4x0 = 0                    2x0=0                  1
#         8         +              0       +                0                  +   1         = 9 decimal base 10

# 2nd method B2d we can find 1001 binay number in decimal  with computer number series 
#       8    4   2    1  
#       1    0   0    1         32 se pehlay 31    so binary 1001 no convert in decimal 8+1 = 9 


#  D2B    9    base 10
#       10x0 = 1
#        1x9 = 9




# CONVERT  OCTAL TO BINARY  which is 4 + 2 +1 = 7   we want for bin 3 digit bcz 421 are 3 digits
#  0,                                0   0   0    yahan pe sary 0 q k upar 0 nhn 421 hai
#  1,                                0   0   1     yahan upar 1 hai is lie 1 
#  2,                                0   1   0     yahan 2 hai upar is lie 1 jo value exist ho uska 1
#  3,                                0   1   1     2+1 = 3 to 2 aur 1 neechay 1,1 
#  4,                                1   0   0       4 upar hai to us ke neechay 1
#  5,                                1   0   1       4+1 = 5 to 4 aur 1 ke neechay 1 , 1
#  6,                                1   1   0         4+ 2 = 6
#  7,                                1   1   1          4+2+1 = 7

   
#  Octal to binary if we have 23 value for octal 8 base we write 0o23
#   2     3        we watch upper octal number 2 and three and write here 2 and three bin
#  010   011

# if we have   101   in octal 0o101
#  1     0      1     we watch upper octal number 1   0    1 and write   
#  001  000   001         NOW same this value convert in decimal 
#  0       0     1        0     0    0      0    0    1    we count 1 to 1 , 1 to 64 is 65 
#  256    128   64      32     16    8     4     2    1    #  NOW the result in decimal 65


#  BINARY TO OCTAL  1000001        we can write in bainay we sparate of 3 ,3 digit 
#    001     000    001       we can write extra 00 at the end for comlete 3 digits
#     1       0      1        watch uppar octal no. result in bin 101  

#  another examlpe   1100111 
#   001       100          111   
#     1        4             7            in octal result 147
#  another examlpe   11011 
#  011         011
#   3           3                     in octal result 33  




# TASK   IN python program we have 101 in octal convert on bin

print(bin(0o101))

# TASK   IN python program we have 101 in bin convert on octal

print(oct(0b101))

#  now i solve this wihout known type
# for decimal print 456 the ans will be same 456
#  This output just integer/decimal because this is tha part of integer/decimal

# 1 Method  The reult is found only integer /decimal
print(456)
print(0o1234)
print(0b010101)
print(0x23f) 
print(0xb49)

#  if we write
# for decimal print 65 the ans will be same 65 These values output will be only decimal

#  2 Method  These values output will be in decimal octal ,binay, hexa
print(65)
print(oct(65))
print(bin(65))
print(hex(65))

#  3 METHOD if we write result in decimal oct hexa bin
print(0x41)
print(oct(0x41))
print(hex(0x41))
print(bin(0b10010111))
#  0 didnt cout 
print(bin(0b00010111))


#  HEXA to BAINARY AND BAINARY TO HEXA 0-->15   8+4+2+1 = 15... ye number series se nikaltay hain 

#          8  4  2  1                          8  4  2  1
# 0        0  0  0  0
# 1        0  0  0  1            10 A          1  0  1  0
# 2        0  0  1  0            11 B          1  0  1  1
# 3        0  0  1  1            12 C          1  1  0  0
# 4        0  1  0  0            13 D          1  1  0  1
# 5        0  1  0  1            14 E          1  1  1  0
# 6        0  1  1  0            15 F          1  1  1  1
# 7        0  1  1  1
# 8        1  0  0  0
# 9        1  0  0  1

#  H2B  41 value in hexa base 16 = 
#    4          1        watch upper binary in 4 and 1 and put down 
#  0100      0001       result in bin = 01000001

#  another example  we write in between 0--15  2D

#  2D is     2      13
#          0010    1101            = 00101101   we ignore first 2 00 then 101101

#  B2H   10011100011  we make set 4 digit in hexa  bcz 8+4+2+1+15 are 4 digits  if we want   1 digit mre then we put 0
#   0100                1110                   0011
#    4                   14                      3   = 4143 base 16 in hexa OR 0x4143

# another example  B2H  101001      pair 4 digit in hexa
#     0010          1001   
#      2             9            = 29 in hexa base 16 OR 0x29 in python
# another example  B2H  10110111      pair 4 digit in hexa
#    1011          0111
#     B              7            =  B7 in hexa base 16 OR 0xB7 in python

#  TASK WE make a program in python using 24 base 16 H2B  conver Hexa to Binary
#   2            4
#  0010        0100            = 100100    first 00 ignore


#  TASK WE make a program in python using 41 base 16 H2B  conver Hexa to Binary
#   4            1
#  0100         0001         = 1000001    first 0 ignore

# 1st Method   H2D HEXA    41   CONVERT IN DECIMAL make 4 , 4 pair   extend with 00,                            
#   128      64    32      16      8      4     2     1    
#     0       0       1     0      1      0     0     1        = 0B00101001   cvrt in hexa  0010 = 2  , 1001 = 9 result 0x29

# 2nd METHOD H2D task H2D 0x41  convert in decimal 65 how is possible 
#   4                          1   hexa base 16 
#   16 power of 1            16 power of o
#     16 x1 = 16               16x0= 1
#     16x4=  64                 1x1=1
#       64          +            1     = 65  is ANS and with decimal bade 10
#  So we can take LCM    16/65 .... 41     16x4=64 remainder 1   then qutiont 4 remaineder 1 is 41

#  D2H 65      in upper binary chart  6 = 0110  , 5 = 0101    make 65  we can solve this type:
#   65          base 10
#   6             5     
#  10x1=10      10x0=1
#  10x6=60      1x5 = 5
#    60     +     5      = 65 this ans is wrong The ANs should be 41 we can take LCM  OR USE below method

#      64    32     16      8      4     2     1
#            1      0      1       0      0     1      32+8+1=41    41 in hexa base 16


#  decimal 65 base 10    convert in octal  
#    6              5
#   10x1=10        10x0=1
#    10      +       1   = 101  base 8 OR 0o101

#    101 base 8 octal watch octal chart of  make pair of 3      1   0    1         4 2 1  
#    1      0       1
#  001     000     001
#  now 001000001 conert in haexa pair of 4  0100  0001    ignore the fisrt 0       
# 8     4      2      1
# 0     0      0      1
# 0     1      0      0    to ab 1,1 jis digit ke neechay aa raha hai us digit ko lena hai to ye hexa ban jaye 41 base 16 OR 0x41
