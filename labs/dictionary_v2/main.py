

import pprint

text = open('emma.w', 'r')

#open the file of textt file
text = text.read()

text = text.lower()

text = text.replace('[ ]','')
text = text.replace('.','')
text = text.replace(',','')
text = text.replace('!','') 
text = text.replace('?','')
text = text.replace('-','')
text = text.replace(';','')
text = text.replace(':','')
text = text.lstrip('\"')
#removes all the punctuation and further filtering

print(text)
words = text.split()

#look at examples for dict to help
a = {}


for count in range (len(words)):
  if words[count] in a:
    a[words[count]]+= 1
  else:
    a[words[count]] = 1
pprint.pprint(a)


