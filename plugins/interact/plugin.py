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
				greetings.extend(morning_greetings)
			elif time.strftime("%H:%M:%S") <= time.strftime("18:00:00"):
				greetings.extend(day_greetings)
			else:
				greetings.extend(night_greetings)

			random_greeting = random.choice(greetings)

			if random.randrange(2):
				random_greeting = random_greeting.lower()

			greeting_message = "%s %s" % (random_greeting, nick)
			cardinal.sendMsg(channel, greeting_message)
			time.sleep(2)


	# def multi_hello(self, cardinal, user, channel, msg):
	# 	question = ['Will you stop with the hello?',
	# 				'I have greet you twice now... will you tell me what you need?',
	# 				'Stop with the hello..'
	# 				'Are you blind? I have already said hi..'
	# 				]
	# 	nick, ident, vhost = user.group(1), user.group(2), user.group(3)
	# 	if user.group(1) == command(['hello']) * 2:
	# 		return cardinal.sendMsg(channel, random.choice(question))


def setup():
    return InteractPlugin()