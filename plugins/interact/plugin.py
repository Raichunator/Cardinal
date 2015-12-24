from cardinal.decorators import command, help
import random
import time

class InteractPlugin(object):
	@command(['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'morning', 'good day'])
	@help("Responds to the user with a greeting.")
	@help("Syntax: hello")

	def hello(self, cardinal, user, channel, msg):
		greetings = ['Hello', 'Hey', 'Hi', 'Cheers', 'Greetings']
		morning_greetings = ['Good morning', 'Morning']
		day_greetings = ['Good afternoon', 'Fine afternoon', 'Good day']
		night_greetings = ['Good evening']
		nick, ident, vhost = user.group(1), user.group(2), user.group(3)
		if command(['hello']):
			if time.strftime("%H:%M:%S") < time.strftime("12:00:00"):
				message = random.choice(morning_greetings)
			elif time.strftime("%H:%M:%S") <= time.strftime("18:00:00"):
				message = random.choice(day_greetings)
			else:
				message = random.choice(night_greetings)
			
			greet = random.choice(greetings)
			cardinal.sendMsg(channel, "%s %s" % (greet, user.group(1)))



def setup():
    return InteractPlugin()