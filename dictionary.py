import re
import action

class Dict(action.Action):

    dictionary = {}

    def perform(self, input):
        text = self.get_text(input)
        if text != None:
            m = re.search("~define ", text)
            n = re.search("~about ", text)
           
            if m != None:    # defining a word
                return self.ircfy(input, self.addWord(text))
            elif n != None:  # retrieving
                return self.ircfy(input, self.retrieveWord(text))

        return None


    def addWord(self, text):
        context = text[len("~define "):len(text)].strip()
        m = re.search(".*?:", context)
        if m == None:
            return "I don't understand"
        word = context[m.start():m.end()-1]
        definition = context[m.end():len(text)].strip()

        self.dictionary[word] = definition
        return "Ok"


    def retrieveWord(self, text):
        key = text[len("~about "):len(text)].strip()
        try:
            return key + ": " + self.dictionary[key]
        except KeyError:
            return "I don't know '" + key + "'"
                    
