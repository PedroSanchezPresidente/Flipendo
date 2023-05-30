import datetime

class FlipendoMessages:

    @staticmethod
    def pingMessage(messageDate, latency):
        time = datetime.datetime.utcnow()
        mtime = messageDate
        mtime = mtime.replace(tzinfo = None)

        miliseconds = round((time - mtime).total_seconds() * 1000)
        seconds = int(miliseconds / 1000)
        miliseconds = miliseconds % 1000
        
        apiLatency = int(float(latency) * 1000)

        return '🏓Latency is ' + str(seconds) + 's ' + str(miliseconds) + 'ms. API Latency is '+ str(apiLatency) + 'ms'




