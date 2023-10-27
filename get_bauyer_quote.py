from urllib.request import urlopen
import re

""" Get a random jack bauer quote from the web """
def get_bauer_from_web():
  url = urlopen("https://www.notrly.com/jackbauer/")
  strng = str(url.read())
  url.close()

  m = re.search("p class=\"fact\".*", strng)
  quote = strng[m.start():m.end()]
  m = re.search(".*fact\">", quote)
  quote = quote[m.end():]
  m = re.search("<.*", quote)
  quote = quote[:m.start()]

  quote = quote.replace("&quot;", "\"")
  quote = quote.replace("\\", "")
  return quote

#quprint get_bauer_from_web()
