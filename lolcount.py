import re
import action
import random

class lolCount(action.Action):

  def __init__(self):
    self.counterfile = "lolz.txt"
    self.sponsors = ['Baruh atah Adonai...']
    self.lolcount = self.readLolCount()
    
  def readLolCount(self):
    f = open(self.counterfile, 'r')
    line = f.readline()
    f.close()
    return int(line)
                                          
  def writeLolCount(self, count):
    f = open(self.counterfile, 'w')
    f.write(str(count))
    f.close()
    return

  def perform(self, command):
    return self.getLols(command)
    
  #search for the string lol, if found increment variable and print count
  def getLols(self, input):    
    
    if (self.get_text(input) == None):
        return
          
    lol_list = ['lol', 'Lol', 'LOL', 'loL', 'lOl', 'lul', 'lawl', 'l0l']
    for i in lol_list:
      m = re.search(i, self.get_text(input))
      if m != None: break
      
    if m != None:
      self.lolcount += 1
      self.writeLolCount(self.lolcount)
      if  re.search('~lolcount', self.get_text(input)) != None:
        s = str(self.lolcount) + " - this LOL count is sponsored by "
        s += self.sponsors[random.randint(0,len(self.sponsors)-1)]
        return self.ircfy(input, s)
    return     
