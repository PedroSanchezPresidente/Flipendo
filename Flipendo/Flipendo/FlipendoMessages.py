import datetime

from FlipendoClass import FlipendoClass

class FlipendoMessages(FlipendoClass):
    def __init__(self, client):
        super().__init__(client)
    
    def pingMessage(self, messageDate):
        """
        Genera el mensaje del comando ping

        Args:
            messageDate: Datetime de creacion del mensaje
            latency: La latencia del cliente

        Return:
            Devuelve el contenido del mensaje para hacer ping
        """

        time = datetime.datetime.utcnow()
        mtime = messageDate
        mtime = mtime.replace(tzinfo = None)

        miliseconds = round((time - mtime).total_seconds() * 1000)
        seconds = int(miliseconds / 1000)
        miliseconds = miliseconds % 1000
        
        apiLatency = int(float(self.client.latency) * 1000)

        return '🏓Latency is ' + str(seconds) + 's ' + str(miliseconds) + 'ms. API Latency is '+ str(apiLatency) + 'ms'




