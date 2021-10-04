
import color
print (color.red("                                   Fahrenheit/Celsius Conversion"))
print ("_____________________________________________________________________________________________")
print("")
Ask = input("-Would you like to convert either " + (color.yellow("[Fahrenheit]") +(" to celsius or " + (color.yellow("[Celsius]") + (" to fahrenheit? ") + (color.magenta("[Yes]") + (" or ") + (color.magenta("[No]")))))))
print("")
if Ask == ("yes") :
 Ask = ("Yes")

if Ask == ("Yes") :
  Answer = input("-Enter " + (color.yellow("[F]") + (" for Fahrenheit conversion or ") + (color.yellow("[C]") + (" for Celsius conversion."))))
  if Answer == ("f") :
   Answer = ("F")
  if Answer == ("c") :
   Answer = ("C")

  if Answer == ("F") :
   print("")
   Fahrenheit = float(input("-Enter your " + (color.yellow("[Fahrenheit°F]") + (" degree :"))))
   Celsius = (float(Fahrenheit - 32)*5/9)
   Celsius = round(Celsius)
   print ("----------------------------------------------------------------------------------------------")
   print ("~ " + str(color.magenta(Celsius) + (color.magenta("°C")+ (" is the degree after the °F to °C conversion"))))
   print ("----------------------------------------------------------------------------------------------")
   print("")
   Ask2 = input("-Would you like to know the exact temperature? " +(color.magenta("[Yes]") + (" or ") + (color.magenta("[No]"))))
   if Ask2 == ("yes") :
     Ask2 = ("Yes")
   if Ask2 == ("Yes") :
     Celsius = (float(Fahrenheit -32)*5/9)
     print ("----------------------------------------------------------------------------------------------")
     print ("~ " + str(color.magenta(Celsius) + (color.magenta("°C") + (" is the exact temperature."))))
     print ("----------------------------------------------------------------------------------------------")
     print ("") 
     print (color.green("Click ") + (color.yellow("[Run]") + (color.green(" to re-convert a degree."))))

  if Answer == ("C") :
   print("")
   Celsius = float(input("-Enter your " + (color.yellow("[Celsius°C]") + (" degree :"))))
   Fahrenheit = (float(Celsius *9/5) +32)
   Fahrenheit = round(Fahrenheit)
   print ("----------------------------------------------------------------------------------------------")
   print ("~ " + str(color.magenta(Fahrenheit) + (color.magenta("°F") + ( " is the degree after the °F to °C conversion"))))
   print ("----------------------------------------------------------------------------------------------")
   print ("")
   Ask2 = input("-Would you like to know the exact temperature? " + (color.magenta("[Yes]") + (" or ") + (color.magenta("[No]"))))
   if Ask2 == ("yes") :
     Ask2 = ("Yes")
   if Ask2 == ("Yes") :
     Fahrenheit = (float(Celsius *9/5) +32)
     print ("----------------------------------------------------------------------------------------------")
     print ("~ " + str(color.magenta(Fahrenheit) + (color.magenta("°F") + (" is the exact temperature."))))
     print ("----------------------------------------------------------------------------------------------")
     print ("")
     print (color.green("Click ") + (color.yellow("[Run]") + (color.green(" to re-convert a degree."))))
else :
  print ("----------------------------------------------------------------------------------------------")
  print (color.red("User chose not to convert or entered invaild answer."))