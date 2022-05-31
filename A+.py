import random

print('Chatbox: What is your name? ')
user_input = input()
print('Hello ' + user_input + ', Nice to meet you, what do you want to know you')

name = 'I.T.K'
weather = 'Rainy'
mood = 'Happy!'

chatbox_template = name + ': {0}'
user_template = user_input + ' : {0}'

response = {
    'what is your name?': [
        'They call me {0}'.format(name),
        'I usually go by {0}'.format(name),
        'Je mapelle {0}'.format(name),
        'You can call me {0}'.format(name),
        'Where is is your manners, You can call me danny{0}'.format(name)],

    'What\'s today\'s weather?': [
        'The weather is {0}'.format(weather),
        'It\'s {0} today'.format(weather),
        'Let me check, it looks {0} today'.format(weather)],

    'Are you a robot?': [
        'What do you think?',
        'Maybe yes, maybe no!',
        'Yes, I am a robot with human feelings.'],

    'How are you?':[
        'I am feeling {0}'.format(mood),
        '{0}! How about yourself?'.format(mood)],
    'default': [
        'This is a default message']
}

def respond(message):
    if message in respond:
        bot_message = random.choice(response[message])
    else:
        bot_message = random.choice

