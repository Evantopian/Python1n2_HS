import pprint

#open text file 
speech = open('speech.txt', 'r')
#save the text to the variable speech

speech = speech.read()


#clean up speech (remove common punctuation)
speech = speech.lower()


speech = speech.replace('.', '')
speech = speech.replace(',', '')
speech = speech.replace('?', '')
speech = speech.replace('!', '')
speech = speech.replace('-', '')

#create a list of each word in the speech
words = speech.split()

print(words)

wordsDict = {}

for i in range(5):
  print()


for i in range(len(words)):
  if words[i] in wordsDict:
    wordsDict[words[i]] += 1
  else:
    wordsDict[words[i]] = 1

print(wordsDict)


for i in range(5):
  print()


pprint.pprint(wordsDict)