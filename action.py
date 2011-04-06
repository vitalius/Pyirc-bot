import re


""" Extract PRIVMSG information """
class Action:

    """ Extract the IRC header information of the message """
    def get_header(self, input):
        
        src = re.search("^:.*?:", input)
        if src != None:
            return input[src.start():src.end()]
        else:
            return None


    """ Extract username if it exists from the IRC command header """
    def get_nickname(self, input):
        
        header = self.get_header(input)
        if header == None:
            return None
        
        # find nickname
        src = re.search("^:.*\!", header)
        if src != None:
            return header[src.start()+1:src.end()-1]
    
        return None


    """ Extract hostname if it exists from the IRC command header """
    def get_hostname(self, input):
        
        header = self.get_header(input)
        if header == None:
            return None
            
        # find hostname
        src = re.search("![^ ]*", header)
        if src != None:
            return header[src.start()+3:src.end()]
    
        return None


    """ Extract channel if it exists from the IRC command header """
    def get_channel(self, input):
        
        header = self.get_header(input)
        if header == None:
            return None
    
        # find channel
        src = re.search("#.*:", header)
        if src != None:
            return header[src.start()+1:src.end()-2]
    
        return None


    """ Extract text if it exists from the IRC command header """
    def get_text(self, input):
        
        header = self.get_header(input)
        if header == None:
            return None

        return input[len(header):len(input)]
        


    """ Sub-classes overwrite this method """
    def perform(self, command):
        return


    """ Format the text according to IRC protocol """
    def ircfy(self, input, text):
        
        if text == None:
            return None
        if (self.get_channel(input) != None):
            return "PRIVMSG #" + self.get_channel(input) + " :" + text.strip() + "\r\n"
        elif (self.get_nickname(input) != None):
            return "PRIVMSG " + self.get_nickname(input) + " :" + text.strip() + "\r\n" 
        return None
    
    def print_info(self, input):
        print "DEBUG: Action requested:"
        if (self.get_nickname(input) != None) : print "  By: " + self.get_nickname(input)
        if (self.get_hostname(input) != None) : print "From: " + self.get_hostname(input)
        if (self.get_channel(input) != None) : print "Chan: " + self.get_channel(input)
        if (self.get_text(input) != None) : print "Text: " + self.get_text(input)


#### DEBUG #####

#line1 = ":go|dfish!n=goldfish@minerva.redbrick.dcu.ie PRIVMSG #ls-dj :lol"
#line2 = ":ezeki3l!i=pavlenko@c-24-22-56-210.hsd1.wa.comcast.net PRIVMSG anna_bot :hi"

#a = Action()
#print a.ircfy(line1, "hello")
#a.print_info(line2)
