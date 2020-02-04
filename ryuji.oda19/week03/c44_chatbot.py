import random

class Bot:
    def __init__(self, bot_name):
        self.b_name = bot_name
        self.phrases = ['Creativity takes courage.',
                        'Your limitation is only your imagination.',
                        'Making mistakes is better than faking perfection.']

    def introduce(self):
        return 'My name is ' + self.b_name + '! I am a BOT!'

    def good_luck(self, u_name):
        return 'Nice to meet you ' +u_name+ '! Good luck for the Bootcamp!'

    def random_quote(self):
        return random.choice(self.phrases)

# bot = Bot('Alexa')
# print(bot.introduce())
# print(bot.good_luck('Siri'))
# print(bot.random_quote())
# print(bot.random_quote())
# print(bot.random_quote())
