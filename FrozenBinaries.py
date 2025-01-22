#  Frozen binaries:
# file tayar honay ke baad client ko kaisay deni hai
#   file bnanayen gay .py 
# Run kartay hain PVM  mashine pe 
# PVM covert karay ga .pyc main compiled python file jisko hum bytecode bhi kahtay hain
#  jab PVM kaam kar le ga means >pyc main convert karay ga to Excute karay ga
#  question : client/user ko kia dena hai .py ki file nhn deni?
#  Ans: hamara jo bhi program hai .py  us pe hum ne third party tool lagana hai, python ne kuch tool banaye hain jasiay woh file tool ko bhejen gay to woh .pyc file banaye ga +pvm ko add  karay ga + other file,  pyc+pvm+otherfile in 3no ko comment kar ke aik single file bana de ga jisko installer kehtay hain ye file client ko den gay, ab client is click kar ke install kar ke run karay ga

#  with the help of third party tool your python program into true executable, Known as frozen binaries in the python world. means third party tool ki madad se hum aik executable gile bana len gay jis ko python ki duniya main frozen binaries kahty hain. yaani aik asisi file jis ko client chalaye ga is lie isko frozen binaries kehtay hain. just hum .exe file den gay client ko.

#  frozen binaries bundle together the bytecode of your program files, along with the help of PVM(intepreter) and any python support files your program needs, into a single package. means frozen binaries bundle karti hai bytecode ko jo program hum ne banaya hai uska bytecode banay ga .pyc se usko bundle karay ga PVM se, us ke sath python support file ye other file bhi .pyc se ttach karni paray gi, in 3no files ka jo pack banaya hai usko frozen binaries kahtay hain yahi installer hota hai yahi client ko dena hota hai.

#  The end result can be a single binaryexecutable program(e.g., an .exe file on the window) that can easily be shipped to customers

#  $$$$$$$$$$$$$$$

#  THIRD PARTY TOOLS:
#  Today a vriety of systems arecapable of generation frozen binaries, which vary in platforms and features like:
# py2app for windows onle. but with broad windows support; agar client widows use kar rha hai to us ke  lie konsa software ya tool use hoga uske lie py2exe ka use karen gay. ye file just windos system pe chalay gi.

# PyInstaller, which is similar to py2exe but also works on Linux and Mac OS X. PyInstaller agar ye tool use karen gay to ye sab pe chalay ga

#  py2app for creating MAC OS X applictions. is software pe bani hoi  file just MAC PE USE HOGI


#  Freeze, and cx_freeze , which offers both Pyhton 3, X and cross-platform support. Freeze ko hi cx_freeze kehtay hain ye dono equalent hain aik dosaray ke, ye offer karta hai jo python ka latest compiler\code aa raha hai yaani latest PVM hoga us ke lie jaisay python 4.9.11 us ke lie banaye ga jo ke aik cross-platform hai yaani  kisi aik/specific  ke lie nhn banaye ga balkay saray cover karay ga, to ye use karna chahiye jo sab ke lie use ho. 
#  apni requirement ke according koi bhi tool le saktay hain

#  jarna kia hai , aik program banana hai .py pe phir  jo upper tools likhay hain unko apply karna hai woh tool aisi file banaye ga jisko client install ya execute karay ga. is tarah se client ko program ya file deliver krna hota hai