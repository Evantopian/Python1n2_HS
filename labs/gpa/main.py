Math = float(input("What's your math avergage?"))
English = float(input("What's your English average?"))
Science = float(input("What's your science average?"))
History = float(input("What's your history average?"))
PE = float(input("What's your physical education average?"))

Average = (float((Math + English + Science + History + PE)/5))

Total = round(Average,2)

print (("Your total avergae is ") + str(Total) + ("!"))