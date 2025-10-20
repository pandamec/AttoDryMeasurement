
class instruments:
    def __init__(self,
                 AttoDry800=True,
                 Keithley800=True,
                 AttoDrySteps=True,
                 LakeShoreMonitor=False)


    def getMeasurement(self):
        """Get the measurement in Table form at the instant"""


        n_point s =Parameters.MeasurementPoints
        sample_rat e =Parameters.SampleRate

        data_total = []
        # initKeithley(Parameters)
        # keithley.set_VoltageRange(defineVoltageRange(T_set))
        # keithley.output_on()

        for i in n_points:
            TS = Atto.sample.getTemperature()
            TC = Atto.tboard.getTemperature(0)
            Q = Atto.sample.getHeaterPower()
            R_sensor = Atto.sample.getResistance()

            # keithley.set_current(strom)
            # Sourcemeter = keithley.get_Mess()
            # V, I, R_sample = getVoltageCurrentResistance(Sourcemeter) V=0
            I=0
            R_sample=0

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
        # keithley.output_off()
        return data_total