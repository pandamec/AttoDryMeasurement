
import time

from .PrologixGPIB import PrologixGPIB

class Device(PrologixGPIB):
    """Keithley 2400 SourceMeter control."""
    def reset(self):
        self.send_instr('*RST')
        time.sleep(0.5)

    def idn(self):
        return self.query('*IDN?')

    #def enable_4wire(self):
     #   self.send_instr(':SYST:RSEN ON')

    #def disable_4wire(self):
     #   self.send_instr(':SYST:RSEN OFF')

    ## Voltage Mode
    #def source_VoltageMode(self):
     #   self.send_instr(':SOUR:FUNC VOLT')
      #  self.send_instr(':SOUR:VOLT:MODE FIXED')

    #def set_voltage(self, value):
     #   self.send_instr(f':SOUR:VOLT {value}')

    #def get_current(self):
     #   self.send_instr(':FORM:ELEM CURR')
      #  return self.query(':READ?')

    #def set_current_compliance(self, value):
     #   self.send_instr(f':SENS:CURR:PROT {value}')

    ## Current Mode

    def enable_4wire(self):
        self.send_instr(':SYST:RSEN ON')

    def source_CurrentMode(self):
        self.send_instr(':SOUR:FUNC CURR')
        self.send_instr(':SOUR:CURR:MODE FIX')

    def set_CurrentRange(self, value):
       self.send_instr(f':SOUR:CURR:RANG {value}')

    def set_current(self, value):
        self.send_instr(f':SOUR:CURR:LEV {value}')

    def set_VoltageCompliance(self, value):
       self.send_instr(f':SENS:VOLT:PROT {value}')


    def set_VoltageSense(self):
        self.send_instr(':SENS:FUNC "VOLT"')
        #self.send_instr(':SENS:FUNC "CURR"')
        #return self.query(':READ?')

    def set_VoltageRange(self, value):
        self.send_instr(f':SENS:VOLT:RANG {value}')
        self.send_instr(':FORM:ELEM VOLT,CURR')

    def get_Mess(self):
        return self.query(':READ?')

    def output_on(self):
        self.send_instr(':OUTP ON')

    def output_off(self):
        self.send_instr(':OUTP OFF')