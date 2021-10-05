#Walking 1:
"""
name = input("What is your name?")
dream = input("Whats your dream job?")
plan = input("Whats your plans for next week's holiday?")
print("")
print("Here's a list of everything you entered.")
print("_______________________________________________________________")
print(name)
print(dream)
print(plan)
"""
#Walking 2:
"""
first = input("Whats your first name?")
last = input("Whats your last name?")
print("")
print("_______________________________________________________________")
print(first + (" ") + last + (", How are you going today?"))
"""
#Jogging 1:
"""
famous_person = ("Jake Paul")
quote = ("It's every day bro with the disney channel flow")
print(famous_person + ':' + '"' + quote + '".')
"""
#Jogging 2:
"""
user_number = input("Give me a number")
if int(user_number)%2 == 0 :
 print("It's Even")
else:
 print("It's Odd!")
"""
#Running 1:
"""
import math
radius = int(input("Can you give me the radius of the circle in order to find the area?"))
area = str(math.pi*(radius*radius))
print(area + ", is the area of your circle! Would you like to figure out another circle's area?")
"""
#Running 2:
"""
Time = int(input("Please enter the amount of seconds you want to convert to\nhours, minutes and seconds."))
Seconds = int(Time%60)
Minutes = int((Time/60)%60)
Hour = int((Time/3600)%60)
print("")
print (str("After the seconds to H/M/S conversion the results are: \n" + str(Hour) + " Hour(s), " ) + str(Minutes) + " Minute(s) and " + str(Seconds) + " Second(s).")
print("")
print("If you would like to convert again please click [Run].")
"""
#Running 3:

Mark = int(input("What did you receive on your previous Exam? (Exam Mark)"))
print("")
if Mark >= 90 :
  print("Whoo! You received a [A]!!!")
elif Mark >= 80 :
  print("Nice! You received a [B]!!!")
elif Mark >= 70 :
  print("Try and work on studying a bit! You received a [C]!!!")
elif Mark >= 60 :
  print("Pay more attention in class! You received a [D]!!!")
elif Mark < 60 :
  print("Welcome to New Utrect! \n\nMy name is Mr. Huang, I'll be your English teacher this summer. \nI pray that you will hopefully pass this, but we all know your future will only have a McDonalds Co-Worker T-Shirt in it.")
else:
  print("Please enter a valid input!")
print("")
print("Click [Run] to restart the program!]")