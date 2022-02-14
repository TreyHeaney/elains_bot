# Accept your brother's forgetfulness as charity.

import discord
import os
from random import choice

from discord.ext import tasks, commands
from dotenv import load_dotenv

from src.timer import Timer

load_dotenv()

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

# client = MyClient()
# client.run()

client = discord.Client()


async def handle_command(command, message):
    if command == 'hello':
        print(message)
        await message.channel.send(f'hello @{message.author}')


@client.event
async def on_ready():
    print(f'loaded as {client.user}')
    timerCog = Timer()


@client.event
async def on_message(message):
    print(dir(client))

    print(dir(message))
    print(f'{message.author} said {message.content}')

    if '😭' in message.content:
        sad_things = ['😭W😭H😭Y😭', '😭', 'NOOOOOOOOOOOOOOOOOOOO WHHHHYYYYYYYY😭😭😭', '😭😭😭']
        await message.channel.send(f'DETECTED SADNESS; RUNNING ROUTINE \"EMPATHY\; {choice(sad_things)}')
    
    words = message.content.split(' ')
    if words[0] == 'bot...':
        handle_command(words[1], message)


client.run(os.getenv('API_KEY'))
