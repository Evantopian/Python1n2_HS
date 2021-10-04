import random


#Working on some other things. if grading dont bother wit dis.
print ("Give 5 numbers that are within or equal to 1-70.")
UserNumber = int(input("Please enter 1 of the numbers"))


for N in range (2,7):

  if 0< UserNumber >71:
    Num = str(N + 1)
    UserNumber = str(UserNumber)
    UserNumber += " " + input((" Please enter ") + (Num) + (" of the number."))
print (UserNumber)


#code
Lottery = "                         "

for L in range (6):
  if L < 5:
    prob = str(random.randrange(70))
    Lottery += prob + " "
  else:
    LDid = str(random.randrange(25))
    Lottery += "[" + LDid + "]"

print (Lottery)