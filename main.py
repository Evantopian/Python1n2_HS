"""



number = int(input("Gimme a number")) 
while number != 1:
  print (number)
  if number == 1:
    break
  if number%2 == 0:
    number = number/2 
  elif number%2 != 0:
    number = (number *3)+1
print (number)

"""

'''
def Graph(t,x):
  Space = []
  for i in range (len(x)):
    a = x[i]
    while (True):
      if t == a:
        a -= 1 
      else:
        Space.append(a)
        print (Space)
        break
  return (Space)
'''

def space(x,t):
  for l in range (t):
    a = ''
    for i in range (len(x)):
      if t - x[i] <= l:
        a += "*\t"
      else:
        a += "\t"
    print (a)






  
      
x = [7,1,8,3]
t = 0
for i in range (len(x)):
  if t < x[i]:
    t = x[i]

space(x,t)

h = ''
for z in range (len(x)):
  h += (str(x[i]),"\t")

