import re
import action

class PingPong(action.Action):

    def perform(self, input):
        m = re.search("^PING", input)
        if m != None:
            return "PONG :" + input[6:len(input)]
        return None

#line1 = "PING :zelazny.freenode.net"

#a = Pong()
#print a.perform(line1)
