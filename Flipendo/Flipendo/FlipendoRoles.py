from FlipendoClass import FlipendoClass

class FlipendoRoles(FlipendoClass):
    def __init__(self, client):
        super().__init__(client)

    def giveRole(self, message):
        """
        Da un rol a un miembro

        Args:
            message: mensaje con el comando
        """

        words = message.content.split(maxsplit=2)
        if(len(words) >= 3):
            roleName = words[1]
            role = self.discord.utils.get(message.guild.roles, name=roleName)
            if(role != None):
                memberName = words[2]
                member = self.discord.utils.get(message.guild.members, name=memberName)
                if(member != None):
                    if(member in role.members):
                        return [message.channel.send('El miembro ' + memberName+ ' ya esta en ese rol.')]
                    else:
                        return [member.add_roles(role, reason=None, atomic=True),
                                message.channel.send(memberName + ' ha sido añadido a ' + roleName + '.')]
                else:
                    return [message.channel.send('No se encrontró el miembro ' + memberName)]
            else:
                return [message.channel.send('No se encrontró el rol ' + roleName)]
        else:
           return [message.channel.send('Se necesita especificar rol y miembro')]

    def takeRole(self, message):
        """
        Quita un rol a un miembro

        Args:
            message: mensaje con el comando
        """

        words = message.content.split(maxsplit=2)
        if(len(words) >= 3):
            roleName = words[1]
            role = self.discord.utils.get(message.guild.roles, name=roleName)
            if(role != None):
                memberName = words[2]
                member = self.discord.utils.get(message.guild.members, name=memberName)
                if(member != None):
                    if(member in role.members):
                        return [member.remove_roles(role, reason=None, atomic=True),
                               message.channel.send(memberName + ' ya no tiene el rol de ' + roleName + '.')]
                    else:
                        return [message.channel.send('El miembro ' + memberName+ ' no esta en ese rol.')]
                else:
                    return [message.channel.send('No se encrontró el miembro ' + memberName)]
            else:
                return [message.channel.send('No se encrontró el rol ' + roleName)]
        else:
            return [message.channel.send('Se necesita especificar rol y miembro')]
            
    def changeRole(self, message):
        """
        Cambia un rol a un miembro

        Args:
            message: mensaje con el comando
        """

        words = message.content.split(maxsplit=3)
        if(len(words) >= 4):
            roleName1 = words[1]
            role1 = self.discord.utils.get(message.guild.roles, name=roleName1)
            if(role1 != None):
                roleName2 = words[2]
                role2 = self.discord.utils.get(message.guild.roles, name=roleName2)
                if(role2 != None):
                    memberName = words[3]
                    member = self.discord.utils.get(message.guild.members, name=memberName)
                    if(member != None):
                        if(member in role1.members):
                            if(member in role2.members):
                                return [message.channel.send('El miembro ' + memberName+ ' ya esta en ese rol.')]
                            else:
                                return [member.remove_roles(role1, reason=None, atomic=True),
                                        member.add_roles(role2, reason=None, atomic=True),
                                        message.channel.send(memberName + ' se le ha cambiado el rol de ' + roleName1 + ' a ' + roleName2+'.')]
                        else:
                            return [message.channel.send('El miembro ' + memberName+ ' no esta en ese rol.')]
                    else:
                        return [message.channel.send('No se encrontró el miembro ' + memberName)]
                else:
                    return [message.channel.send('No se encrontró el rol ' + roleName2)]
            else:
                return [message.channel.send('No se encrontró el rol ' + roleName1)]
        else:
            return [message.channel.send('Se necesita especificar rol antiguo, rol nuevo y miembro')]




