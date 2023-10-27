import re
import action

class Stfu(action.Action):
    
    def __init__(self):
        return
    
    def perform(self, command):
            return self.getTime(command)

    def getTime(self, input):
        if (self.get_text(input) == None):
            return
        m = re.search("~stfu", self.get_text(input))
        if m != None:
            return "MUTE 120" # in seconds
        return
