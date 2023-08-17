from xml.etree.ElementTree import tostring

import discord
from FlipendoMessages import FlipendoMessages


#Example code
intents = discord.Intents.default()
intents.members = True
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
        elif message.content.startswith('!help'):
            await message.channel.send('Todabía está en desarrollo')

        #Comando give
        elif message.content.startswith('!give'):
            #await message.channel.send('Todabía está en desarrollo')
            words = message.content.split(maxsplit=3)
            if(len(words) >= 3):
                roleName = words[1]
                role = discord.utils.get(message.guild.roles, name=roleName)
                if(role != None):
                    memberName = words[2]
                    member = discord.utils.get(message.guild.members, name=memberName)
                    if(member != None):
                        await member.add_roles(role, reason=None, atomic=True)
                        await message.channel.send(memberName + ' ha sido añadido a ' + roleName + '.')
                    else:
                        await message.channel.send('No se encrontró el miembro ' + memberName)
                else:
                    await message.channel.send('No se encrontró el role ' + roleName)
            else:
                await message.channel.send('Se necesita especificar rol y miembro')
            
        #Comando take
        elif message.content.startswith('!take'):
            await message.channel.send('Todabía está en desarrollo')

        #Comando change
        elif message.content.startswith('!change'):
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
