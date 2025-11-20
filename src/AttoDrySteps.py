class AttoDrySteps:
    def __init__(self,
                 TestMode: int,
                ControlMode: int,
                TimeControlMode:int,
                Temperaturen:list[float],
                TimeStep: int):

        self.TestMode = TestMode
        self.ControlMode = ControlMode
        self.TimeControlMode = TimeControlMode
        self.Temperaturen = Temperaturen
        self.TimeStep = TimeStep

        if TestMode == 2:
            T_target = sorted(self.Temperaturen, reverse=True)

        else:
            T_target = sorted(self.Temperaturen)
        self.TargetTemperaturen=T_Target
            

    def simulation(self):

        total = []
        # n=0
        total_T = []
        accu = 0
        if Parameters.TestMode == 1:
            delta = (2 * 3600) / (300 - 5)
            T_current = 5
            for i in Parameters.TargetTemperaturen:
                accu = accu + Parameters.TimeStep + Parameters.TimeMeasurement * len(
                    Parameters.Strom) + Parameters.TimeSleepCurrent * len(Parameters.Strom) + (i - T_current) * delta
                total.append(accu)
                total_T.append(i)
                T_current = i

        else:
            delta = (8 * 3600) / (300 - 5)
            T_current = 293
            for i in Parameters.TargetTemperaturen:
                accu = accu + Parameters.TimeStep + Parameters.TimeMeasurement * len(
                    Parameters.Strom) + Parameters.TimeSleepCurrent * len(Parameters.Strom) + (T_current - i) * delta
                total.append(accu)
                total_T.append(i)
                T_current = i

        time = np.linspace(0, round(total[-1]), round(total[-1]))
        Temp = []
        time2 = []
        Temp_coldplate = []
        time_trigger = 0
        for n in range(0, len(total), 1):
            for i in time:
                if i <= total[n] and i > time_trigger:
                    time2.append(i)
                    Temp.append(total_T[n])
                    Temp_coldplate.append(total_T[n] - computeColdplateTemperature(total_T[n]))
                    time_trigger = i
        # Temperaturen=Parameters.TargetTemperaturen
        # Temp=[]
        # Temp_coldplate=[]
        # t=0
        # n=0
        # Time_increment=Parameters.TimeStep + Parameters.TimeMeasurement * len(Parameters.Strom) + Parameters.TimeSleepCurrent * len(Parameters.Strom)
        # for ii in T:
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
        # else:
        #  Temp.append(Temperaturen[n])
        #  Temp_coldplate.append(Temperaturen[n]-computeColdplateTemperature(Temperaturen[n]))

        return time2, Temp, Temp_coldplate

    def plotSimulation(self):
        s = simulation(Parameters)
        T = np.array(s[0])
        Temp = s[1]
        Temp_coldplate = s[2]
        # Create the first plot with the first y-axis
        fig, ax1 = plt.subplots(figsize=(12, 6))

        ax1.plot(T / 3600, Temp, label='Sample-plate temperature', color='red')
        ax1.plot(T / 3600, Temp_coldplate, label='Cold-plate temperature', color='blue')
        ax1.set_xlabel('Time (hours)')
        ax1.set_ylabel('Temperature (K)')
        ax1.tick_params(axis='y')

        # Show the plot
        plt.title('Simulation')
        plt.legend()
        plt.show()


    def computeColdplateTemperature(T):
        """Set the minimum delta required between the sample and coldplate based september 25 measurement"""
        ## von abkühlung
        if 75 < T <= 300:
            delta = 10
        elif 50 < T <= 75:
            delta = 15
        elif 25 < T <= 50:
            delta = 10
        elif T <= 25:
            delta = 5

        return delta


    def getcoolingrate(t):
        """Compute the cooling rate in a  determined delta time t"""
        TS1 = Atto.sample.getTemperature()
        time.sleep(t)
        TS2 = Atto.sample.getTemperature()

        dTds = (TS2 - TS1) / t

        return dTds


    def getcoolingrateExchange(t):
        """Compute the cooling rate in a  determined delta time t"""
        TS1 = Atto.exchange.getTemperature()
        time.sleep(t)
        TS2 = Atto.exchange.getTemperature()

        dTds = (TS2 - TS1) / t

        return dTds


    def perform_approach(self):
        """Perform an approach to the set temperature value. The transition should be smooth close to the set temperature value"""

        t_limitColdPlate = 1 * 3600
        t_limitSamplePlate = 1.5 * 3600
        dTds = getcoolingrateExchange(1)  # Time step 1s
        T_targetSample = T_target
        T_target = T_target - computeColdplateTemperature(T_target)
        Ts = Atto.exchange.getTemperature()
        Delta = T_target - Ts

        print("performing an approach")
        print("Target value in Coldplate", T_target)

        count = 0
        n_dTds = 0
        if mode_test == 1:  ## Erwärmung
            while n_dTds < 10:  # with 0.001 it got stuck.  It was a case with 7.998 which was higher than 0.001 delta. That means, T set remained as  +dTds*-5
                T_set = T_target

                print(T_set)
                startControl(T_set, T_target, mode_control)

                dTds = getcoolingrate(2)

                Ts = Atto.sample.getTemperature()

                Delta = T_target - Ts
                if abs(dTds) <= 0.0001:
                    n_dTds = n_dTds + 1

        elif mode_test == 2:  ## Abkühlung

            while n_dTds < 5 and count <= t_limitColdPlate:

                if 1 < -Delta <= 10:
                    T_set = T_target + dTds * -30

                elif 0.01 < -Delta <= 1:
                    T_set = T_target + dTds * -20

                elif -Delta <= 0.01:
                    T_set = T_target + dTds * -10
                else:
                    T_set = T_target

                print("T_set value", T_set)
                print("Coolingrage", dTds)

                startControlExchange(T_set)
                startControl(T_targetSample, T_targetSample, mode_control)
                if abs(dTds) <= 0.01:
                    n_dTds = n_dTds + 1

                dTds = getcoolingrateExchange(2)
                Ts = Atto.exchange.getTemperature()
                Delta = T_target - Ts
                count = count + 1
            startControlExchange(T_target)

            print("approach finished Cold Plate")
            n_dTds = 0

            while n_dTds < 10 and count <= t_limitSamplePlate:

                T_set = T_target

                startControl(T_targetSample, T_targetSample, mode_control)

                dTds_Sample = getcoolingrate(2)

                if abs(dTds_Sample) <= 0.005:
                    n_dTds = n_dTds + 1
                count = count + 1

            print("approach finished")
        return

    def stopControl(mode_Control):
        """Stop the temperature control"""
        Atto.sample.stopTempControl()
        if mode_Control == 2:
            Atto.exchange.stopTempControl()

    def startControlExchange(Temperature):
        """Start the temperature control"""

        Atto.exchange.setSetPoint(
            Temperature)  # Previously coldplate directly -20 wrt the set temperature. this created an oscillation on the sample temperature value after 10min
        Atto.exchange.startTempControl()

    def startControl(Temperature, T_target, mode_control):
        """Start the temperature control"""

        Atto.sample.startTempControl()
        Atto.sample.setSetPoint(Temperature)
        if mode_control == 2:
            Atto.exchange.setSetPoint(Temperature - computeColdplateTemperature(
                Temperature))  # Previously coldplate directly -20 wrt the set temperature. this created an oscillation on the sample temperature value after 10min
            Atto.exchange.startTempControl()

    def startTest(self,getMeasurement):
        """Start the test"""
        log_total = []
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

        df_logtotal = pd.DataFrame(log_total)
        df_logtotal.to_csv(Parameters.Filename, index=False)


        print(log_total)

        Atto.sample.stopTempControl()
        Atto.exchange.stopTempControl()
