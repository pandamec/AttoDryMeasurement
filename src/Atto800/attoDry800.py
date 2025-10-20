from . import ACS
from .system import System
from .exchange import Exchange
from .pumpValve import Pumpvalve
from .pressures import Pressures
from .about import About
from .network import Network
from .action import Action
from .sample import Sample
from .access import Access
from .sampleValve import Samplevalve
from .main import Main
from .functions import Functions
from .turboPump import Turbopump
from .breakVacuumValve import Breakvacuumvalve
from .system_service import System_service
from .membranePump import Membranepump
from .update import Update
from .tboard import Tboard
from .compressor import Compressor


class Device(ACS.Device):
    def __init__(self, address):
        super().__init__(address)

        self.system = System(self)
        self.exchange = Exchange(self)
        self.pumpValve = Pumpvalve(self)
        self.pressures = Pressures(self)
        self.about = About(self)
        self.network = Network(self)
        self.action = Action(self)
        self.sample = Sample(self)
        self.access = Access(self)
        self.sampleValve = Samplevalve(self)
        self.main = Main(self)
        self.functions = Functions(self)
        self.turboPump = Turbopump(self)
        self.breakVacuumValve = Breakvacuumvalve(self)
        self.system_service = System_service(self)
        self.membranePump = Membranepump(self)
        self.update = Update(self)
        self.tboard = Tboard(self)
        self.compressor = Compressor(self)
        
        

def discover():
    return Device.discover("attodry800")
