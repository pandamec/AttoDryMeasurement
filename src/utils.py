from datetime import datetime
import time

def setFilename(Designation):
    """ Set the name of the file"""
    today = datetime.now()
    datum = today.strftime("%Y%m%d%H")

    filename = str(datum) + "_" + Designation
    print(filename)

    return filename


def getMeasurement(Atto,keithley,Monitor):
    """Get the measurement in Table form at the instant"""

    TS = Atto.sample.getTemperature()
    TC = Atto.tboard.getTemperature(0)
    Q = Atto.sample.getHeaterPower()
    R_sensor = Atto.sample.getResistance()

    data = {
        'Time[s]': datetime.now().timestamp(),
        'Cold-Plate[K]': TC,
        'Sensor Resistance[Ohm]': R_sensor,
        'Sample Temperature[K]': TS,
        'Sample Heat[W]': Q,
        'Set Temperature[K]': T_set}

    if keithley.Status==True:
        V,Set_I,I,R=keihtley.getVoltageCurrentResistance()

        data['Voltage [V]']= V,
        data['Set Current [I]']= Set_I,
        data['Current [I]']= I,
        data['Sample Resistance [Ohm]']= R

    if Monitor.status==True:
        T_monitor=Monitor.getTemperature()

        data['Monitor Temperature [K]']= T_monitor

    return data

def startTest(Atto,AttoSteps,keithley,Monitor,File):

    """Start the test"""
    log_total = []
    triggered = set()

    TS = Atto.sample.getTemperature()

        for i in AttoSteps.T_target:

            if AttoSteps.TestMode == 1: #Erwärmung
                condition = TS <= i
            else:
                condition = TS >= i

            if condition and i not in triggered:
                print(f"\n==> T close to Target {i} K found. Starting control.")
                triggered.add(i)

                perform_SimpleApproach(i)

                if keithley.Status==True:
                    for strom_target in keithley.Strom:
                        keithley.setCurrent(strom_target)

                log = getMeasurement(Atto,keithley,Monitor)  # Get the measurement
                log_total.extend(log)
                time.sleep(keithley.TimeSleepCurrent)
                print(log)

            TS = Atto.sample.getTemperature()
    df_logtotal = pd.DataFrame(log_tota)
    df_logtotal.to_csv(File, index=False)


