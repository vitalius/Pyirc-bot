import re
import action
import time

class Tyme(action.Action):
	
	def __init__(self):
		return
	
	def perform(self, command):
        	return self.getTyme(command)

	def getTyme(self, input):
		if (self.get_text(input) == None):
			return
		m = re.search("~tyme", self.get_text(input))
		if m != None:
			tyme = time.localtime(time.time())
			str_tyme = str( time.asctime(tyme) )
			return self.ircfy(input, str_tyme)
		return
