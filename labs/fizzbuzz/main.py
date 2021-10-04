
# FizzBuzz, Accumalative calculator, FizzBuzz Accumalative and Prime. 




#FIZZBUZZ
"""
for Number in range (1,10):
  if Number % 3 == 0 and Number % 5 == 0:
    print ("FizzBuzz!!!")
  elif Number % 3 == 0:
    print ("Fizz!")
  elif Number % 5 == 0:
    print ("Buzz!")
  else:
    print ("Oof big neck! The number was: "+ str(Number))
"""

"""
#ACCUMALATIVE CALCULADORA

Number = int(input("Number? "))
Calculate = 0
Number = Number + 1
for N in range (0,Number):
  Calculate = Calculate + N

print (Calculate)
"""


#FIZZBUZZ ACCUMALATIVE
"""
Calculate = 0
Store = 0
for Number in range (1,1000):
  if Number % 3 == 0 and Number % 5 == 0:
    Store = Number + Store
  elif Number % 3 == 0:
    Store = Store + Number
  elif Number % 5 == 0:
    Store = Store + Number
  else:
    Calculate = Number + Calculate

print (Calculate)
print (Store)
"""




#PRIME NUMBRE"
N = int(input("Give me a number"))
if N > 1:
  for X in range(2,N):
    print ()
    if (N % X) == 0:
     print(N,"is not a Prime number.")  
     break
  else:
     print ("It's Prime.")
else:
  print(N, "is not a Prime number, it's Composite.")

  
  
  