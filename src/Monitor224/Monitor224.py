from lakeshore import Model224
ip='192.168.1.12'
monitor = Model224(ip_address = ip)

class device:
    def __init__(self,
                 channel):
        self.channel=channel

    def getTemperature(self):
        T= monitor.get_kelvin_reading(self.channel)

        return T



