import sys
sys.path.append(r"E:\00 Script\Attodry800.Characterization\src")
import Atto800

IP = "192.168.1.1"
Atto=Atto800.Device(IP)
Atto.connect()



def initiateAttoDry():

    return 1

def startCoolingDown():
    Atto.action.goToBase()

def startSamplePlate(T):
    Atto.sample.setSetPoint(T)
    Atto.sample.startTempControl()


def startColdPlate(T):
    Atto.exchange.setSetPoint(T)
    Atto.exchange.startTempControl()

def stopControl():
    Atto.sample.stopTempControl()
    Atto.exchange.stopTempControl()

def getSampleTemperature():
    T=Atto.sample.getTemperature()
    return T

def getColdPlateTemperature():
    T=Atto.exchange.getTemperature()
    return T
