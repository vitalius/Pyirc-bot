import urllib
import re

""" Get a random jack bauer quote from the web """
def get_bauer_from_web():
  url = urllib.urlopen("http://www.notrly.com/jackbauer/")
  strng = url.read()
  url.close()

  m = re.search(".*p class=\"fact\".*", strng)
  quote = strng[m.start():m.end()]
  m = re.search(".*\">", quote)
  quote = quote[m.end():]
  m = re.search("<.*", quote)
  quote = quote[:m.start()]

  quote = quote.replace("&quot;", "\"");
  return quote

#print get_bauer_from_web()
