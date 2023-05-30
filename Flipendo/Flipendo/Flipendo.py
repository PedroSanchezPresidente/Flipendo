from xml.etree.ElementTree import tostring

import discord
from FlipendoMessages import FlipendoMessages


#Example code
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!👍')

    if message.content.startswith('$ping'):
        await message.channel.send(FlipendoMessages.pingMessage(message.created_at, client.latency))

client.run('your token here')
