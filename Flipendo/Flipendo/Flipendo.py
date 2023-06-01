from xml.etree.ElementTree import tostring

import discord
from FlipendoMessages import FlipendoMessages


#Example code
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

#Crea un mensaje al cargar
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Eventos al recibir mensajes
@client.event
async def on_message(message):
    #Ignora los mensajes propios
    if message.author == client.user:
        return

    #Detecta el simbolo de comando
    if message.content.startswith('!'):

        #Comando ping
        if message.content.startswith('!ping'):
            await message.channel.send(FlipendoMessages.pingMessage(message.created_at, client.latency))

        #Comando help
        if message.content.startswith('!help'):
            await message.channel.send('Todabía está en desarrollo')

        #Comando give
        if message.content.startswith('!give'):
            await message.channel.send('Todabía está en desarrollo')
            
        #Comando take
        if message.content.startswith('!take'):
            await message.channel.send('Todabía está en desarrollo')

        #Comando change
        if message.content.startswith('!change'):
            await message.channel.send('Todabía está en desarrollo')

        #En caso de no encontrar el comando
        else:
            #Si el mesaje esta vacio
            if len(message.content) == 1:
                await message.channel.send('Escribe !help para información')

            else:
                await message.channel.send('No hay ningun comando '+ str(message.content)[1:].split()[0] +'. Escribe !help para información')

#Corre el cliente
client.run('your token here')
