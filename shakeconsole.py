
from textindex import textindex
import os



fileName="shakespeare.txt"
sIndex=textindex(fileName)

word = input("Enter a word to search for:")
matches=sIndex.lookupLinesText(word)

for line in matches:
  print(line)