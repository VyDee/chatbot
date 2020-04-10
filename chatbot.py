from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# advice
# Create a new chat bot named Charlie
bot = ChatBot('Cat')
bot.storage.drop()
trainer = ListTrainer(bot)
for _file in os.listdir('chat'):
    chats = open('chat/'+ _file, encoding="utf8").readlines()
    trainer.train(chats)

#clear storage


while True:
    request = input('You: ')
    response = bot.get_response(request)
    print('Bot: ', response)