import discord

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

# client = MyClient()
# client.run()

client = discord.Client()

@client.event
async def on_ready():
    print(f'lol {client.user}')

@client.event
async def on_message(message):
    print(f'{message.author} said {message.content}')
    print(dir(message))

client.run('OTQyMTgwOTI5OTk1MTUzNDYw.YggwXg.J0I2pk6vFaGiv8F2hWUfYTDd9v0')