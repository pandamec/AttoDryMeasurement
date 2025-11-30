import sys
sys.path.append(r"E:\00 Script\Attodry800.Characterization\src")
import Atto800

IP = "192.168.1.1"
Atto=Atto800.Device(IP)
Atto.connect()

def initiateAttoDry():

    return 1

def startSamplePlate(T):
    Atto.sample.startTempControl(T)

def startColdPlate(T):
    Atto.exchange.setSetPoint(T)

def stopControl():
    Atto.sample.startTempControl()
    Atto.exchange.startTempControl()

def getSampleTemperature():
    T=Atto.sample.getTemperature()
    return T

def getColdPlateTemperature():
    T=Atto.exchange.getTemperature()
    return T