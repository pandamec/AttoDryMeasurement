def startSamplePlate(T):
    Atto.sample.startTempControl(T)

def startColdPlate(T):
    Atto.exchange.setSetPoint(T)

def stopControl():
    Atto.sample.startTempControl()
    Atto.exchange.startTempControl()

def getSampleTemperature():
    Atto.sample.getTemperature()

