import serial
import time

class PrologixGPIB:
    """Base class for Prologix GPIB-USB controller."""
    def __init__(self, port, gpib_addr):
        baudrate = 115200
        timeout = 1
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.gpib_addr = gpib_addr
        self.configure_adapter()

    def configure_adapter(self):
        """Configure Prologix settings."""
        self.send_raw('++mode 1')                 # Controller mode
        self.send_raw(f'++addr {self.gpib_addr}') # GPIB address
        self.send_raw('++auto 0')                 # Manual read
        self.send_raw('++eoi 1')                  # Assert EOI
        self.send_raw('++eos 3')                  # CR+LF endings

    def send_raw(self, cmd):
        """Send a raw command to Prologix or instrument."""
        self.ser.write((cmd + '\n').encode())
        time.sleep(0.05)

    def send_instr(self, cmd):
        """Send a SCPI command to the instrument."""
        self.send_raw(cmd)

    def read_instr(self):
        """Read one line of response from the instrument."""
        return self.ser.readline().decode().strip()

    def query(self, cmd):
        """Send a query and return the instrument's response."""
        self.send_instr(cmd)
        self.send_raw('++read eoi')
        return self.read_instr()

    def close(self):
        self.ser.close()