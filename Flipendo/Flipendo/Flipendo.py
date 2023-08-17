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
            words = message.content.split(maxsplit=2)
            if(len(words) >= 3):
                roleName = words[1]
                role = discord.utils.get(message.guild.roles, name=roleName)
                if(role != None):
                    memberName = words[2]
                    member = discord.utils.get(message.guild.members, name=memberName)
                    if(member != None):
                        if(member in role.members):
                            await message.channel.send('El miembro ' + memberName+ ' ya esta en ese rol.')
                        else:
                            await member.add_roles(role, reason=None, atomic=True)
                            await message.channel.send(memberName + ' ha sido añadido a ' + roleName + '.')
                    else:
                        await message.channel.send('No se encrontró el miembro ' + memberName)
                else:
                    await message.channel.send('No se encrontró el rol ' + roleName)
            else:
                await message.channel.send('Se necesita especificar rol y miembro')
            
        #Comando take
        elif message.content.startswith('!take'):
            words = message.content.split(maxsplit=2)
            if(len(words) >= 3):
                roleName = words[1]
                role = discord.utils.get(message.guild.roles, name=roleName)
                if(role != None):
                    memberName = words[2]
                    member = discord.utils.get(message.guild.members, name=memberName)
                    if(member != None):
                        if(member in role.members):
                            await member.remove_roles(role, reason=None, atomic=True)
                            await message.channel.send(memberName + ' ya no tiene el rol de ' + roleName + '.')
                        else:
                            await message.channel.send('El miembro ' + memberName+ ' no esta en ese rol.')
                    else:
                        await message.channel.send('No se encrontró el miembro ' + memberName)
                else:
                    await message.channel.send('No se encrontró el rol ' + roleName)
            else:
                await message.channel.send('Se necesita especificar rol y miembro')

        #Comando change
        elif message.content.startswith('!change'):
            words = message.content.split(maxsplit=3)
            if(len(words) >= 4):
                roleName1 = words[1]
                role1 = discord.utils.get(message.guild.roles, name=roleName1)
                if(role1 != None):
                    roleName2 = words[2]
                    role2 = discord.utils.get(message.guild.roles, name=roleName2)
                    if(role2 != None):
                        memberName = words[3]
                        member = discord.utils.get(message.guild.members, name=memberName)
                        if(member != None):
                            if(member in role1.members):
                                if(member in role2.members):
                                    await message.channel.send('El miembro ' + memberName+ ' ya esta en ese rol.')
                                else:
                                    await member.remove_roles(role1, reason=None, atomic=True)
                                    await member.add_roles(role2, reason=None, atomic=True)
                                    await message.channel.send(memberName + ' se le ha cambiado el rol de ' + roleName1 + ' a ' + roleName2+'.')
                            else:
                                await message.channel.send('El miembro ' + memberName+ ' no esta en ese rol.')
                        else:
                            await message.channel.send('No se encrontró el miembro ' + memberName)
                    else:
                        await message.channel.send('No se encrontró el rol ' + roleName2)
                else:
                    await message.channel.send('No se encrontró el rol ' + roleName1)
            else:
                await message.channel.send('Se necesita especificar rol antiguo, rol nuevo y miembro')

        #En caso de no encontrar el comando
        else:
            #Si el mesaje esta vacio
            if len(message.content) == 1:
                await message.channel.send('Escribe !help para información')

            else:
                await message.channel.send('No hay ningun comando '+ str(message.content)[1:].split()[0] +'. Escribe !help para información')

#Corre el cliente
client.run('your token here')
