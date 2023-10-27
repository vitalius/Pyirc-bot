import re
import action
import random
import get_bauyer_quote

class Bauer(action.Action):
    def __init__(self):
        return

    def perform(self, command):
        return self.bauerFact(command)

    def bauerFact(self, input):
        m = re.search("~bauer",str(input))
        
        if m != None:
            return self.ircfy(str(input), get_bauyer_quote.get_bauer_from_web())

