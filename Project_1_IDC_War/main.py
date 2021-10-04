import random

def Game(P1Name,P2Name,deckNumber):
  def Multipler(deckNumber,DeckValue):
    DeckValue = deckNumber * 4
    return(DeckValue)

  def Shuffle(DeckValue):
    Deck = list(range(2,15))* DeckValue
    for S in range (49):
      random.shuffle(Deck)
    return (Deck)


  def SplitFor1(DeckValue,Deck):
    SplitValue = int((13*DeckValue)/2)
    Split1 = []
    Deck1 = []
    for I in range (SplitValue*2):
      Deck1.append(Deck[I])
    for I in range (SplitValue):
      Split1.append(Deck1[I])
      Deck1.remove(Deck1[I])
    return (Split1)

  def SplitFor2(DeckValue,Deck):
    SplitValue = int((13*DeckValue)/2)
    Split2 = []
    Deck2 = []
    for I in range (SplitValue*2):
      Deck2.append(Deck[I])
    for I in range (SplitValue):
      Deck2.remove(Deck2[I])
      Split2.append(Deck2[I])
    return (Split2)


  def Deal1(P1V,War1):
    if (len(P1V)) > 4:
      L = 4
    else:
      for I in range(len(P1V)):
        L = I+1
    War1.append(P1V[0:L])
    return(War1)

  def Deal2(P2V,War2):
    if (len(P2V)) > 4:
      L = 4
    else:
      for I in range(len(P2V)):
        L = I +1
    War2.append(P2V[0:L])
    return(War2)
  DeckValue = 0
  DeckValue = Multipler(deckNumber,DeckValue)
  Deck = Shuffle(DeckValue)
  Split1 = SplitFor1(DeckValue,Deck)
  Split2 = SplitFor2(DeckValue,Deck)
  turns = 0
  Game = True

  def Win(P1V,P2V,turns,P1Name,P2Name,Score1,Score2):
    if P1V == []:
      print ("\n\n\nScore of players's: ",Score1, "-", Score2)
      print (P2Name, "Won the War! Oof to", P1Name,"!")
      print (P1Name,"'s deck: " , P1V,"\n")
      print (P2Name, "'s deck: ", P2V)
      print ("\n\n---------------\nTotal turns|", turns)
      print (len(P1V),len(P2V))
      return True

    if P2V == []:
      print ("\n\n\nScore of players's: ",Score1, "-", Score2)
      print (P1Name, "Won the War! Oof to", P2Name, "!")
      print (P1Name,"'s deck: " , P1V,"\n")
      print (P2Name, "'s deck: ", P2V)
      print ("\n\n---------------\nTotal turns|", turns)
      print (len(P1V),len(P2V))
      return True

      
  Score1 = 0
  Score2 = 0
  P1V = Split1
  P2V = Split2
  while Game:
    turns += 1
    War1 = []
    War2 = []

    War1 = Deal1(P1V,War1)
    War2 = Deal2(P2V,War2)

    print ("_________________________________\nP1: ", War1[-1], "-    P2: ", War2[-1])

    if War1[-1] == War2[-1]:
      print ("War!!!!AJAJAJA")
      Score1 += 1
      Score2 += 1

    if War1[-1] > War2[-1]:
      print (P1Name,"has the greater card! Cards seized!")
      Score1 += 1
      P1V.extend(War1)
      P1V.extend(War2)

    if  War1[-1] < War2[-1]:
      print (P2Name,"has the greater card! Cards seized!")
      Score2 += 1
      P2V.extend(War1)
      P2V.extend(War2)
    if Win(P1V,P2V,turns,P1Name,P2Name,Score1,Score2) == True:
      break
    

Ask = input("Would you like to play war?")
if Ask in ("Yes","yes","Y","y"):
  P1Name = input("What's player 1's name?")
  P2Name = input("What's player 2's name?")
  deckNumber = int(input("How many decks would you like to play with?"))
  Game(P1Name,P2Name,deckNumber)
else:
  print ("Addio")

