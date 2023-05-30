import datetime
from time import timezone
from xml.etree.ElementTree import tostring

import discord
from datetime import date, tzinfo


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

    if message.content.startswith('$pin2'):
        time = datetime.datetime.utcnow()
        mtime = message.created_at
        mtime = mtime.replace(tzinfo = None)

        miliseconds = round((time - mtime).total_seconds() * 1000)
        seconds = int(miliseconds / 1000)
        miliseconds = miliseconds % 1000
        
        apiLatency = int((float(client.latency) * 1000) % 1000)

        await message.channel.send('🏓Latency is ' + str(seconds) + 's ' + str(miliseconds) + 'ms. API Latency is '+ str(apiLatency) + 'ms')

client.run('your token here')
