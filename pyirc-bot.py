import socket
import sys
import time

import say
import bauer
import tyme
import pingpong
import dictionary
import lolcount
import stfu
import bs_generator
import awesomeness
import fortune
import shakespearean_insult

LIVE = 0
MUTE = 1

class PyIRCbot:

  """ Initialize local variables
  Arguments
     server   - hostname of the server
     port     - port number
     nickname - nickname for the bot
     channel  - channel to join
     
  socket - open network stream for IRC
  status - holds information about bot state """
  def __init__(self, server, port, nickname, channel):
    self.socket = None
    self.nickname = nickname
    self.channel = channel
    self.status = 1
    self.buffer = None
    self.buffsize = 4096
    self.actions = []

    self.state = LIVE
    self.mute_start = 0
    self.mute_finish = 0
    self.duration = 0
    
    self.connect(server, port)

  """ Build a TCP/IP connection to the irc server specified by 'host' and 'port'
  connection is made based on the RFC protocol
  http://www.irchelp.org/irchelp/rfc/chapter4.html#c4_1_2 """
  def connect(self, host, port):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    self.socket.connect((host,port))
    self.sendData("NICK " + self.nickname + " \r\n")
    self.sendData("USER w00t tolmoon tolson :Ronnie Reagan \r\n")
    self.sendData("JOIN #" + self.channel + " \r\n")

  
  """ Send data to socket stream if a connection was made """  
  def sendData(self, data):
    if self.socket == None:
      print("Error: Non-existing socket")
      return

    self.socket.send(data.encode('utf-8'))
    return


  def installAction(self, act):
    self.actions.append(act)

  def setMute(self, inputStr):
    if len(inputStr) == 8 and inputStr[0:4] == "MUTE":
      self.mute_start = time.time()+ int(inputStr[5:8])
      self.mute_finish = self.mute_start + self.duration
      self.state = MUTE
    return
  
  def checkMute(self):
    if (self.mute_finish < time.time()):
      self.state = LIVE
      return False
    return True
   
  """ Reads and returns the socket buffer, specified by the 'buffsize' """
  def readData(self):
    if self.socket == None:
      print("Error: Non-existing socket")
      return
    
    self.buffer = self.socket.recv(self.buffsize)
    return self.buffer


  """ Running the bot """
  def run(self):
    buf = self.readData()
    while len(buf) > 0:
      # Run action.perform on all actions in the list
      # and if there are any results, write them to socket
      for a in self.actions:
        if a.get_nickname(buf) == self.nickname:
          break
        result = a.perform(str(buf))
        if result != None:
          self.setMute(result) # check mute flag
          if self.checkMute() == False:
            self.sendData(result)
          print(result.strip())
          
      buf = self.readData()
      print(buf.strip()) # log, print everything to stdout

while True:
  try:
    ircbot = PyIRCbot("irc.libera.chat", 6667, "adom-gadol", "israel")
    ircbot.installAction(say.Say())
    ircbot.installAction(bauer.Bauer())
    ircbot.installAction(tyme.Tyme())
    ircbot.installAction(pingpong.PingPong())
    ircbot.installAction(dictionary.Dict())
    ircbot.installAction(lolcount.lolCount())
    ircbot.installAction(stfu.Stfu())
    ircbot.installAction(bs_generator.BS())
    ircbot.installAction(awesomeness.Awesomeness())
    ircbot.installAction(fortune.Fortune())
    ircbot.installAction(shakespearean_insult.SI())
    ircbot.run()
  except:
    pass
