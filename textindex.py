import string

def removePunctuation(s):
  "Remove all punctuation from a string"
  for c in string.punctuation:
    s= s.replace(c,"")
  return s

def convertQuotes(s):
  ''' changes double quotes to two single quotesfor proper JSON encoding '''
  s = s.replace('"','\'\'')
  return s
  
def addToIndex(index,word,line):
  ''' Add a index for a found word to the dict '''
  if word not in index:
    index[word]=[line] # make new entry
  else:
    #The following checks if the word was already found on the line
    if line not in index[word]:
      index[word].append(line)

class textindex:
  ''' A class for indexing words and looking up matches '''
  def __init__(self,filename):
    '''Create a dictionary of all words, with the key being the word, and the value being the number of times the word is found '''
    self.index={}
    self.filename = filename
    self.inFile = open(filename,"r")
    pos=0
    line=self.inFile.readline()
    while len(line)>0:
      line=line.strip().lower()
      line=removePunctuation(line.lower())
      words=line.split()
      for word in words:
        addToIndex(self.index,word,pos)
      pos=self.inFile.tell()  # Next line position
      line=self.inFile.readline()
    return

  def wordcount(self):
    ''' Return the number of lines '''
    return len(self.index)

  def lookupLine(self,pos):
    ''' Lookup line from index in file '''
    self.inFile.seek(pos,0)
    line = self.inFile.readline().strip()
    return line
    
  def lookupLinesText(self,word):
    ''' Return a jason list of lines with matching words '''
    word=word.lower()
    lines = []
    if word in self.index:
      posList=self.index[word]
      for l in posList:
        line = self.lookupLine(l)
        lines.append(line)
    return lines  

  def lookupLinesJSON(self,word):
    ''' Return a jason list of lines with matching words '''
    word=word.lower()
    lines = "{\"matches\":["
    if word in self.index:
      posList=self.index[word]
      print(posList)
      for l in posList:
        line = self.lookupLine(l)
        if '"' in line:
          print(line)
          line = convertQuotes(line)
          print(line)
        lines += "\""+line+"\","
      lines=lines[:-1]
    lines += "]}"
    return lines  



  
