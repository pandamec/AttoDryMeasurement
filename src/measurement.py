from src.Keithley4wire import keithley4wire


class measurement:
    def __init__(self,
                 Atto,
                 keithley,
                 AttoDrySteps,
                 keithley4wire,
                 StatusAttoDry800=True,
                 StatusKeithley2400=True,
                 StatusAttoDrySteps=True,
                 StatusLakeShoreMonitor=False)

        self.Atto=Atto
        self.StatusAttoDry800=StatusAttoDry800
        self.StatusKeithley=StatusKeithley2400
        self.StatusAttoDrySteps=StatusAttoDrySteps
        self.StatusLakeShoreMonitor=StatusLakeShoreMonitor

    def getMeasurement(self, T_set, strom):
        """Get the measurement in Table form at the instant"""


        n_point s =Parameters.MeasurementPoints
        sample_rat e =Parameters.SampleRate

        data_total = []

        keithley4wire.initiate(self)
        keithley.set_VoltageRange(keithley4wire.defineVoltageRange(T_set))
        keithley.output_on()

        for i in n_points:
            TS = Atto.sample.getTemperature()
            TC = Atto.tboard.getTemperature(0)
            Q = Atto.sample.getHeaterPower()
            R_sensor = Atto.sample.getResistance()

            V=0
            I=0
            R_sample=0
            if self.StatusKeithley==True:
                keithley.set_current(strom)
                Sourcemeter = keithley.get_Mess()
                V, I, R_sample = keithley4wire.getVoltageCurrentResistance(Sourcemeter)

            data = {
                'Time[s]': datetime.now().timestamp(),
                'Cold-Plate[K]': TC,
                'Sensor Resistance[Ohm]': R_sensor,
                'Sample Temperature[K]': TS,
                'Sample Heat[W]': Q,
                'Set Temperature[K]': T_set,
                'Voltage [V]': V,
                'Set Current [I]': strom,
                'Current [I]': I,
                'Sample Resistance [Ohm]': R_sample
            }

            time.sleep(sample_rate)
            data_total.append(data)
        keithley.output_off()

        return data_total

    def startTest(self, getMeasurement):
        """Start the test"""
        log_total = []
        # log_total = firstMeasurement(getMeasurement,Parameters)
        triggered = set()

        ## Calibration

        TS = Atto.sample.getTemperature()

        for i in Parameters.TargetTemperaturen:

            if Parameters.TestMode == 1:
                condition = TS <= i
            else:
                condition = TS >= i

            if condition and i not in triggered:
                print(f"\n==> T close to Target {i} K found. Starting control.")
                triggered.add(i)

                perform_approach(Parameters.TestMode, Parameters.ControlMode, i)

                time.sleep(Parameters.TimeStep)  # Waiting time for starting the measurement after the settling time
                for strom_target in Parameters.Strom:
                    log = getMeasurement(i, Parameters, strom_target)  # Get the measurement
                    log_total.extend(log)
                    time.sleep(Parameters.TimeSleepCurrent)
                    print(log)

            TS = Atto.sample.getTemperature()
            if Parameters.TestMode == 2:
                stopControl(Parameters.ControlMode)

            # df_logtotal=pd.DataFrame(log_total)
            # df_logtotal.to_csv(filename, index=False)
        # print(log_total)
        df_logtotal = pd.DataFrame(log_total)
        df_logtotal.to_csv(Parameters.Filename, index=False)

        # time.sleep(5) # Compare each 5s

        #   if len(triggered) == len(T_target):
        #      print("All temperature controls completed.")
        #     break

        print(log_total)

        Atto.sample.stopTempControl()
        Atto.exchange.stopTempControl()
        # keithley.output_off()

