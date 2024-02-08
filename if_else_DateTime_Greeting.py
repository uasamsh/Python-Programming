
#import time
        
import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)
  

# for Separate Hour and Minute Seconds
timestampe =int(time.strftime("%H"))
print(timestampe)

timestamp=int(time.strftime("%M"))
print(timestamp)

timestamp=int(time.strftime("%S"))
print(timestamp)



# Certainly! Below is a Python program that greets the user according to the time of the day:

import datetime

def greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 0 >= hour < 12:
        print("Good morning!")
    elif 12 <= hour < 18:
        print("Good afternoon!")
    elif 18 <= hour < 22:
        print("Good evening!")
    else:
        print("Good night!")

# Call the greeting function
greeting()


# Date time and month
import datetime

def date_time_month():
 current_datetime=datetime.datetime.now()
 current_time=current_datetime.strftime("%H:%M:%S")
 current_date=current_datetime.strftime("%Y-%m-%d")
 current_month=(current_datetime.strftime("%B"))

 print( "Current Time : ", current_time)
 print("Current Date is : ", current_date )
 print("Current Month is : ", current_month)

date_time_month() 


