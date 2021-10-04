import color
#Imports a color function into the code to make it cool *Cough* EXTRA Credit :D

print((color.yellow)("                                   Project #1" + (" (Pluralizer)")))
print("____________________________________________________________________________________________________")
print("")
#Just the title with a touch of color and a space to make it extra fancy

word = input((color.magenta)("Please enter a word for the computer to pluralize :)"))
#Variable that is set to whatever noun the user inputs into the program.
number = int(input((color.magenta)("How many of the inputs are there?")))
#variable that is set to whatever number of noun there are. (Will display the number of nouns in the chained conditonals later on.)

Last1 = word[-1:]#Sets to the last 1 letters of the noun.
Last2 = word[-2:]#Sets to the last 2 letters of the noun.
Last3 = word[-3:]#Sets to the last 3 letters of the noun.

print("")
#3 variables with a space to make it more "pleasing" to look at. You could call this my style.

if number > 1 :
  #If statement that checks if the number of nouns is greater than 1. If not, program will skip to the Else statement.

  #------------------------------------------------------
  #Chained Conditionals on what the last letters of the noun is. If a ending matches with the letter provided. Then, it would display the plural form.
  if Last1 == "f":
    print ((color.green)("There are  ")+ str(number) + (" ") + (color.yellow)(word[:-1]) + (color.yellow)("ves"))
  
  elif Last3 == "Bus" or Last3 == "bus":
    print((color.green)("There are ") + str(number) + (" ") + (color.yellow)(word) + (color.yellow)("es"))
  
  elif word[-4:] == "oose":
    print((color.green)("There are ") + str(number) + (" ") + (color.yellow)(word[:1]) + (color.yellow)("eese"))

  elif word[-4:] == "ooth":
    print((color.green)("There are ") + str(number) + (" ") + (color.yellow)(word[:1]) + (color.yellow)("eeth"))
  
  elif word[-4:] == "ouse":
    print((color.green)("There are ") + str(number) + (" ") + (color.yellow)(word[:1]) + (color.yellow)("ices"))
  
  #For 4 special cases of words that aren't pluralized like normal nouns. For example, oose is for the word Goose to Geese.

  elif word[-2:] == "fe":
    print ((color.green)("There are ") + str(number) +(" ")+ (color.yellow)(word[:-2]) + (color.yellow)("ves"))

  elif Last2 == "sh" or Last2 == "ch":
    print((color.green)("There are ") + str(number) + (" ") + (color.yellow)(word) + (color.yellow)("es"))

  elif Last2 == "us":
    print((color.green)("There are ")+str(number)+(" ")+ (color.yellow)(word[:-2]) + (color.yellow)("i"))

  elif Last2 == "uy" or Last2 == "oy" or Last2 == "ey" or Last2 == "ay":
    print ((color.green)("There are ") + str(number) + (" ") + (color.yellow)(word) + (color.yellow)("s"))

  # Or statements help organize and minimize the space that is required to program this code considering that most nouns have simmilar plural forms.

  elif Last1 == "y":
    print ((color.green)("There are ") + str(number) + (" ") + (color.yellow)(word[:-1]) + (color.yellow)("ies"))

  #"Normal" nouns that are pluralized for the majority of nouns. For example any word that ends with y would showcase ies. But, the order was set to that the y condition wouldnt contridict with the codes that end with y but require 2 ending letters.

  else:
    print ((color.green)("There are ") + str(number) + (" ") + (color.yellow)(word) + (color.yellow)("s"))
  #This statement runs only when the chained conditionals above don't deem true. It would set the noun with the ending of S.
 
else:
  #This else is the else statement that connects with the first if statement. If the if statement was deemed false, it would run the code below.

  if number == 1:
   print ((color.green)("There is only ") + str(number) + (" ") + (color.yellow)(word) + (color.yellow)("."))
   
  #If the number is equal to 1 then the nouns wouldnt be pluralized. It would show the original inputted noun with the number that was given, 1.

  elif number == 0:
   print ((color.green)("There are no ") + (color.yellow)(word) + (color.yellow)("s."))

  #If the if statement above was not true then it would run else if statement to see if it equals 0. If it is true then, it would pluralize the word with a s at the end and remove the number by replacing it with a text message stated above.

  else:
    print ((color.red)("Either you have a invalid input or you're numbers are in the negatives."))
  
  #This code is the last option due to the fact that there is no other condtions that meet the input. It tells the use the issue, in this case being that it's either false or the numbers inputted are negative because you can't have negative amounts of something.

print("____________________________________________________________________________________________________")
#Just a cool like to make the code EXTA cool

print (("Click ")+ (color.green)("[Run]") + (" to restart the program!"))

#No, this is not a button that you can click. The [GREEN] "Run" resembles the Run button on the top center of the REPL page. 
  


    

