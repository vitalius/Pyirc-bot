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
		
		facts = ['Superman wears Jack Bauer pajamas.', 
'Withholding information from Jack Bauer is now classified as a suicide attempt.', 
'When a convicted terrorist was sentenced to face Jack Bauer, he appealed to have the sentence reduced to death.',
'Jack Bauers calender goes from March 31st to April 2nd, no one fools Jack Bauer.',
'Upon hearing that he was played by Kiefer Sutherland, Jack Bauer killed Sutherland.  Jack Bauer gets played by no man.',
'Jack Bauer could strangle you with a cordless phone.',
'Jack Bauer doesn\'t have a firewall on his PC. He has a Bauerwall. It\'s basically just a JPEG of Jack Bauer. No virus has ever attacked Jack Bauer\'s PC. Ever.',
'Jack Bauer thinks the word mercy just means \"quick interrogation.\"',
'Jack Bauer played Russian Roulette with a fully loaded gun and won.',
'Jack Bauer once won a game of Connect 4 in 3 moves.',
'Jack Bauer doesn\'t take fingerprints, he takes fingers.',
'Bauer is not word, it is a sentence...A death sentence.',
'Killing Jack Bauer doesn\'t make him dead. It just makes him angry.',
'There is the right way, the wrong way, and the Jack Bauer way.  It\'s basically the right way but faster and more deaths.',
'Jack Bauer is the leading cause of death in Middle Eastern men.',
'Jack Bauer was never addicted to heroin. Heroin was addicted to Jack Bauer.',
'Superman\'s only weakness is Kryptonite. Jack Bauer laughs at Superman for having a weakness.',
'When Jack Bauer took a stress test, the test failed.',
'Jack Bauer does not let women on top during sex.  Why?  Because Jack Bauer never fucks up.',
'Jack Bauer once visited the Virgin Islands. They are now The Islands.',
'At last years Christmas party, Jack Bauer brought the punch. Nobody survived.',
'The Black Eyed Peas were just The Peas until Jack Bauer heard their music.',
'When you go to hell, it\'s just a room with you and Jack.',
'People with amnesia still remember Jack Bauer.',
'When you open a can of whoop-ass, Jack Bauer jumps out.',
'The answer is Jack Bauer, the question doesn\'t matter.',
'Jack Bauer can leave a message before the beep.',
'Jack Bauer arm once wrestled Superman. The stipulations were the loser had to wear his underwear on the outside of his pants.',
'Jack Bauer wasn\'t born, he was unleashed.',
'When Jack Bauer used Herbal Essences, the shampoo had an orgasm.',
'Guns dont kill people, Jack Bauer kills people.',
'Your attraction to Jack Bauer in no way affects your sexual orientation.',
'Jack Bauer ended The Never Ending Story.',
'Jack and Jill went up the hill. Only Jack came down. Jill was a fucking terrorist.',
'Jack Bauer once forgot where he put his keys. He then spent the next half-hour torturing himself until he gave up the location of the keys.',
'There were originally five horsemen of the apocalypse. Jack Bauer said he would travel by foot.',
'When Kim Bauer lost her virginity, Jack found it and put it back.',
'Jack Bauer doesn\'t miss. If he didn\'t hit you it\'s because he was shooting at another terrorist twelve miles away.',
'Jack Bauer has been to Mars. Thats why there\'s no life on Mars.',
'Upon hearing that he was played by Kiefer Sutherland, Jack Bauer killed Sutherland. Jack Bauer gets played by no man.',
'Superman has Jack Bauer pajamas.',
'When life hands Jack Bauer Lemons, he kills Terrorists. Jack Bauer fuckin\' hates lemonade.',
'Every time you masturbate Jack Bauer kills a terrorist. Keep up the good work men.',
'Some people see the glass as half full. Others see it as half empty. Jack Bauer see the glass as a deadly weapon.',
'Once, someone tried to tell Jack Bauer a "knock knock" joke. Jack Bauer found out who was there, who they worked for, and where the goddamned bomb was.',
'The 2007 budget for the US Military covers Jack Bauer, two pistols and four billion rounds of ammunition.',
'When Jack Bauer ran out of ammo, he caught 3 bullets in his chest and used them to reload.',
'Jack Bauer doesn\'t have a firewall on his PC. He has a Bauerwall. It\'s basically just a JPEG of Jack Bauer. No virus has ever attacked Jack Bauer\'s PC. Ever.',
'Jack Bauer sleeps with a pillow under his gun.',
'The Berlin Wall fell because Jack Bauer needed to get to the other side.',
'Explosions do not kill Jack Bauer, they just get stuff out of his way.',
'Jack Bauer is the \'i\' in team.',
'Nostradamus once predicted in his journal: \"In the century 21st, the one known as Jacques will be the savior of the world... five seasons in a row.\" Moments later, Jack Bauer knocked down the door, shot Nostradamus in the kneecaps, and yelled \"WHO ARE YOU WORKING FOR?!\"',
'Jack Bauer once stepped into quicksand. The quicksand couldn\'t escape and nearly drowned.',
'There are two hands that can beat a royal flush. Jack Bauer\'s right hand and Jack Bauer\'s left hand.',
'Jack Bauer never retreats, he just attacks in the opposite direction.',
'Jack Bauer doesn\'t have a refresh button on his web browser. All events take place in real time.',
'Bauer is not word, it is a sentence...A death sentence.',
'There are no such thing as lesbians, just women who never met Jack Bauer.',
'When Batman is in trouble, he turns on the  Jack Bauer signal.',
'Jack Bauer asked for a gun and a can of Red Bull. He ate the gun and killed five terrorists. The purpose of the Red Bull remains unknown.',
'Jack Bauer was able to eliminate Bird Flu playing Duck Hunt.',
'Jack Bauer once double teamed a girl.. by himself.',
'Jack Bauer doesn\'t get busy signals. No one is too busy to talk to Jack Bauer.',
'Jack Bauer can hit two birds with no stones.',
'Strippers tip Jack Bauer.',
'Jack Bauer has shot more men in the face than Elton John.',
'If at first you don\'t succeed then your name is not Jack Bauer.',
'There is only one rule for dating Jack Bauer\'s daughter. Don\'t.',
'Jack Bauer does not use birth control he simply demands that you not get pregnant.',
'If you spell Jack Bauer in a Scrabble game you win. Forever.',
'Jack Bauer scared the black out of Michael Jackson.',
'Jack Bauer killed Kenny.']

		m = re.search("~bauer",input)

		if m != None:
                        return self.ircfy(input, get_bauyer_quote.get_bauer_from_web())
			#return self.ircfy(input, facts[random.randint(0, len(facts)-1)])

