import re
import action
import time
import random


""" Randomly say 'You are awesome' to somebody """
class Awesomeness(action.Action):
	
	def __init__(self):
		self.nicknames = {}
                self.quotes = ["You are awesome", 
                               "I totally agree", 
                                "Keep up the good work you are awesomeness", 
                                "Yes! I agree, you're awesome", 
                                "Nobody could have said it better!"]
		return
	
	def perform(self, command):
        	return self.checkName(command)

        def pick_rand(self, lst):
                return lst[random.randint(0,len(lst)-1)]

	def pickAwsmCount(self):
		return random.randint(1,40)

	def checkAwsm(self, n):
		if self.nicknames[n] < 0:
			self.nicknames[n] = self.pickAwsmCount()
			return True
		return False

	def checkName(self, input):
		nick = self.get_nickname(input)
		if nick == None:
			return
		
		if self.nicknames.has_key(nick):
			self.nicknames[nick] -= 1
		else:
			self.nicknames[nick] = self.pickAwsmCount()

		if self.checkAwsm(nick):
			return self.ircfy(input, ""+nick+", "+self.pick_rand(self.quotes)+"!")
		return

