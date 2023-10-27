import re

import action

class Say(action.Action):

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
        m = re.search("~say ", str(input).strip())           # look for the '~say' flag
        if m != None:
            return input[m.end():len(input)].replace("\\r\\n\'","")    # if found, return whatever follows after it
        return None

