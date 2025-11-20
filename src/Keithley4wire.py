class keithley4wire:

    def __init__(self,keithley,
                 VoltageRange,
                 CurrentRange:float,
                 VoltageCompliance:int,
                 Strom: list[float],
                 TimeMeasurement:int,
                 TimeSleepCurrent:int,
                 SampleRate:int):

        self.VoltageRange=VoltageRange
        self.CurrentRange=CurrentRange
        self.VoltageCompliance=VoltageCompliance
        self.Strom=Strom
        self.TimeMeasurement=TimeMeasurement
        self.TimeSleepCurrent=TimeSleepCurrent
        self.SampleRate=SampleRate


    def defineVoltageRange(self,T):
        triggered = 0
        for i in self.VoltageRange:

            if T <= i[0] and triggered == 0:
                Range = i[1]
                triggered = i[1]
        return Range

    def initiate(self):
        keithley.enable_4wire()
        keithley.source_CurrentMode()
        keithley.set_CurrentRange(self.CurrentRange)
        keithley.set_VoltageCompliance(self.VoltageCompliance)
        keithley.set_VoltageSense()

    def getVoltageCurrentResistance(messung):
            """Get the voltage and current from the file exported by Sourcemeter Keithley"""
            parts = messung.split(',')

            # Convert the string parts to floats

            VoltageCurrent = [float(part) for part in parts]
            V = VoltageCurrent[0]
            I = VoltageCurrent[1]
            Ohm = V / I

        return V, I, Ohm