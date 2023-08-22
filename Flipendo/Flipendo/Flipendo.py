from xml.etree.ElementTree import tostring

import discord
from FlipendoMessages import FlipendoMessages
from FlipendoRoles import FlipendoRoles


#Example code
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents = intents)
flipendoMessages = FlipendoMessages(client)
flipendoRoles = FlipendoRoles(client)

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
            await message.channel.send(flipendoMessages.pingMessage(message.created_at))

        #Comando help
        elif message.content.startswith('!help'):
            await message.channel.send('Todabía está en desarrollo')

        #Comando give
        elif message.content.startswith('!give'):
            functions = flipendoRoles.giveRole(message)
            for f in functions:
                await f
            
        #Comando take
        elif message.content.startswith('!take'):
            functions = flipendoRoles.takeRole(message)
            for f in functions:
                await f

        #Comando change
        elif message.content.startswith('!change'):
            functions = flipendoRoles.changeRole(message)
            for f in functions:
                await f

        #En caso de no encontrar el comando
        else:
            #Si el mesaje esta vacio
            if len(message.content) == 1:
                await message.channel.send('Escribe !help para información')

            else:
                await message.channel.send('No hay ningun comando '+ str(message.content)[1:].split()[0] +'. Escribe !help para información')

#Corre el cliente
client.run('your token here')
