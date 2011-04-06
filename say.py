import re

import action

class Say(action.Action):

    def __init__(self):
        return

    """ command - IRC text line, example ...
           :ezeki3l!i=pavlenko@c-24-22-56-210.hsd1.wa.comcast.net PRIVMSG #ls-dj :~say w00t
        extract 'text' from the command line and evaulate with parse() method """
    def perform(self, command):
        extracted_text = self.get_text(command) # extract text part from the irc line
        if (extracted_text != None):
            result = self.parse(extracted_text) # evaluate the text, parse what to say
            if result != None:
                return self.ircfy(command, result)  # format the result to IRC protocol and return
        return None

    def parse(self, input):
        m = re.search("~say ", input)           # look for the '~say' flag
        if m != None:
            return input[m.end():len(input)]    # if found, return whatever follows after it
        return None

#i = ":ezeki3l!i=pavlenko@c-24-22-56-210.hsd1.wa.comcast.net PRIVMSG #testb0tchannel :~say asf"
#u = ":ezeki3l!i=pavlenko@c-24-22-56-210.hsd1.wa.comcast.net PRIVMSG #ls-dj :~say w00t"
#n = Say()
#print n.perform(i)
