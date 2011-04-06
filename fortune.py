import re
import random
import action

class Fortune(action.Action):

    def __init__(self):
        return

    def perform(self, command):
        extracted_text = self.get_text(command) # extract text part from the irc line
        if (extracted_text != None):
            result = self.parse(extracted_text) # evaluate the text, parse what to say
            if result != None:
                return self.ircfy(command, result)  # format the result to IRC protocol and return
        return None

    def parse(self, input):
        m = re.search("~should", input)   
        if m != None:
            return self.rand()

    	m = re.search("~would", input)
	if m != None:
	    return self.rand() 
	    
	m = re.search("~is", input)
	if m != None:
	    return self.rand()

        return None


    def rand(self):
        lst = ["Yes!", "Defenetly NO!", "Maybe...", "Ask me again, later"]
        return lst[random.randint(0,len(lst)-1)]
	
