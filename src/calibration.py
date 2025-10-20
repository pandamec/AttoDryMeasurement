import pandas as pd
from datetime import datetime
from dataclasses import dataclass
import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.f2py.crackfortran import endifs


@dataclass
class TestParameters:
    name: str
    TestMode: int
    ControlMode: int
    TargetTemperaturen: list[float]
    TimeStep: int
    VoltageRange:list[tuple[int, int]]
    CurrentRange:float
    VoltageCompliance:float
    Strom: list[float]
    TimeMeasurement: int
    TimeSleepCurrent: int
    SampleRate: float
    MeasurementPoints: list[float]
    Filename: str


def simulation(Parameters):

    total = []
    #n=0
    total_T=[]
    accu=0
    if Parameters.TestMode==1:
        delta=(2*3600)/(300-5)
        T_current=5
        for i in Parameters.TargetTemperaturen:
            accu=accu+Parameters.TimeStep+Parameters.TimeMeasurement*len(Parameters.Strom)+Parameters.TimeSleepCurrent*len(Parameters.Strom)+(i-T_current)*delta
            total.append(accu)
            total_T.append(i)
            T_current=i

    else:
        delta = (8 * 3600)/(300 - 5)
        T_current=293
        for i in Parameters.TargetTemperaturen:
            accu = accu+ Parameters.TimeStep + Parameters.TimeMeasurement * len(Parameters.Strom) + Parameters.TimeSleepCurrent * len(Parameters.Strom)  +(T_current - i) * delta
            total.append( accu)
            total_T.append(i)
            T_current = i



    time = np.linspace(0, round(total[-1]), round(total[-1]))
    Temp=[]
    time2=[]
    Temp_coldplate = []
    time_trigger=0
    for n in range(0,len(total),1):
        for i in time:
            if i<=total[n] and i>time_trigger:
                time2.append(i)
                Temp.append(total_T[n])
                Temp_coldplate.append(total_T[n] - computeColdplateTemperature(total_T[n]))
                time_trigger=i
   # Temperaturen=Parameters.TargetTemperaturen
    #Temp=[]
    #Temp_coldplate=[]
    #t=0
    #n=0
    #Time_increment=Parameters.TimeStep + Parameters.TimeMeasurement * len(Parameters.Strom) + Parameters.TimeSleepCurrent * len(Parameters.Strom)
    #for ii in T:
     #   if ii<=t+Time_increment:
     #       Temp.append(Temperaturen[n])
     #       Temp_coldplate.append(Temperaturen[n]-computeColdplateTemperature(Temperaturen[n]))
     #   else:
     #       t=t+Time_increment
     #       if n+1<len(Temperaturen):
      #          Temp.append(Temperaturen[n])
      #          Temp_coldplate.append(Temperaturen[n]-computeColdplateTemperature(Temperaturen[n]))
       #         n=n+1
              #  if n==0:
              #      Time_increment=abs(Temperaturen[1] - Temperaturen[0] ) * delta
              #  else:
              #      Time_increment = abs(Temperaturen[n] - Temperaturen[n-1]) * delta
            #else:
              #  Temp.append(Temperaturen[n])
              #  Temp_coldplate.append(Temperaturen[n]-computeColdplateTemperature(Temperaturen[n]))

    return time2,Temp, Temp_coldplate

def plotSimulation(Parameters):
    s=simulation(Parameters)
    T=np.array(s[0])
    Temp = s[1]
    Temp_coldplate = s[2]
    # Create the first plot with the first y-axis
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(T/3600, Temp, label='Sample-plate temperature', color='red')
    ax1.plot(T/3600, Temp_coldplate, label='Cold-plate temperature', color='blue')
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('Temperature (K)')
    ax1.tick_params(axis='y')


    # Show the plot
    plt.title('Simulation')
    plt.legend()
    plt.show()

def bestätigung(Parameters):
    """Confirm the test parameters before starting"""
    """Test mode 1 means measurement during the heating up, 2 during the cooling down"""
    """Control mode 1 means only sample-plate control, 2 means both sample and cold-plate control"""

    t = 0
    for i in Parameters.TargetTemperaturen:
        t = t + Parameters.TimeStep+Parameters.TimeMeasurement*len(Parameters.Strom)+Parameters.TimeSleepCurrent*len(Parameters.Strom)

    print("The estimated time to complete the test is min " + str(
        t / 3600) + " hours" + " (Time for reaching the target temperature not considered)")

    if Parameters.TestMode == 1:
        print("The measurement will be carried out during the heating up")
    else:
        print("The measurement will be carried out during the cooling down")

    print("The following temperatures will be set (in this order) " + str(Parameters.TargetTemperaturen))

    if Parameters.ControlMode == 1:
        print("Only the temperature of the sample plate will be controlled")
    else:
        print(
            "Both temperature of the sample plate and cold plate will be controlled. If the mode is heating up, the cold plate has to be cooled down again until 4 K after the measurement is completed.")

def setT_target(mode_test,Temperaturen):
    """Set the temperature targets and sort"""
    if mode_test == 2:
        T_target = sorted(Temperaturen, reverse=True)

    else:
        T_target = sorted(Temperaturen)

    return T_target

def setFilename(Designation):
    """ Set the name of the file"""
    today = datetime.now()
    datum = today.strftime("%Y%m%d%H")

    filename = str(datum) + "_" + Designation
    print(filename)

    return filename

def getVoltageCurrentResistance(messung):
    """Get the voltage and current from the file exported by Sourcemeter Keithley"""
    parts = messung.split(',')

    # Convert the string parts to floats

    VoltageCurrent = [float(part) for part in parts]
    V = VoltageCurrent[0]
    I = VoltageCurrent[1]
    Ohm = V / I

    return V, I, Ohm

def getMeasurementpoints(TimeMeasurement, SampleRate):
    """Compute the points where the measurement will be carried out"""
    points = int(TimeMeasurement / SampleRate)
    n_points = np.linspace(1,TimeMeasurement, points)
    return n_points

def computeColdplateTemperature(T):
    """Set the minimum delta required between the sample and coldplate based september 25 measurement"""
    ## von Oyuka bis 250917 Heizung 1
    if 75 < T <= 300:
        delta = 20
    elif 50 < T <= 75:
        delta = 15
    elif 25 < T <= 50:
        delta = 10
    elif T <= 25:
        delta = 5

    return delta

def startControl(Temperature, T_target, mode_control):
    """Start the temperature control"""
    Atto.sample.setSetPoint(Temperature)
    Atto.sample.startTempControl()
    if mode_control == 2:
        Atto.exchange.setSetPoint(T_target - computeColdplateTemperature( T_target))  # Previously coldplate directly -20 wrt the set temperature. this created an oscillation on the sample temperature value after 10min
        Atto.exchange.startTempControl()

def stopControl(mode_Control):
    """Stop the temperature control"""
    Atto.sample.stopTempControl()
    if mode_Control==2:
        Atto.exchange.stopTempControl()

def getcoolingrate(t):
    """Compute the cooling rate in a  determined delta time t"""
    TS1=Atto.sample.getTemperature()
    time.sleep(t)
    TS2=Atto.sample.getTemperature()

    dTds=(TS2-TS1)/t
    return dTds

def perform_approach(mode_test, mode_control, T_target):
    """Perform an approach to the set temperature value. The transition should be smooth close to the set temperature value"""
    # startControl(T_target, mode_control)
    dTds = getcoolingrate(1) #Time step 1s
    Ts = Atto.sample.getTemperature()
    Delta = T_target - Ts

    if mode_test == 1: ## Erwärmung
        while Delta >= 0.0001:  # with 0.001 it got stuck.  It was a case with 7.998 which was higher than 0.001 delta. That means, T set remained as  +dTds*-5
            if Delta > 10:
                T_set = T_target
            elif Delta <= 10:

                T_set = T_target + dTds * -10
            elif Delta < 5:
                T_set = T_target + dTds * -5

            elif Delta < 0.05:
                T_set = T_target

            startControl(T_set, T_target, mode_control)

            time.sleep(5)
            dTds = getcoolingrate(1)
            Ts = Atto.sample.getTemperature()
            Delta = T_target - Ts

    elif mode_test == 2: ## Abkühlung

        while -Delta >= 0.0001:  # with 0.001 it got stuck.  It was a case with 7.998 which was higher than 0.001 delta. That means, T set remained as  +dTds*-5
            # if -Delta>10:
            #   T_set=T_target
            if -Delta <= 10:

                T_set = T_target + dTds * -10
            elif -Delta < 5:
                T_set = T_target + dTds * -5

            elif -Delta < 0.05:
                T_set = T_target

            startControl(T_set, T_target, mode_control)

            time.sleep(5)
            dTds = getcoolingrate(1)
            Ts = Atto.sample.getTemperature()
            Delta = T_target - Ts

    return

