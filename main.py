User = input("What's your name?")
Weight = float(input("What is your weight?"))
Height = float(input("What is your height in inches?"))

Height2 = float(Height**2)
Calculate = float((Weight/Height2)*703)
BMI = round(Calculate,2)

print("")
print ((User) + (", your BMI is: ") + str(BMI) + ("!"))

if BMI >= 40:
  print("You're way to obese! Class 3!")
elif BMI >= 35:
  print("You're very obese! Class 2!")
elif BMI >= 30:
  print("You're obese!")
elif BMI >= 25:
  print("You're overweight!")
elif BMI >= 18.5:
  print("You're normal weight!")
else:
  print("You're underweight!")
print ("See you again!")

