@dataclass
class TestParameters:
    name: str
    Filename: str


@dataclass
class AttoDryParameters:

    TestMode: int
    ControlMode: int
    TargetTemperaturen: list[float]
    TimeStep: int

@dataclass
class SourcemeterParameters:

    VoltageRange:list[tuple[int, int]]
    CurrentRange:float
    VoltageCompliance:float
    Strom: list[float]
    TimeMeasurement: int
    TimeSleepCurrent: int
    SampleRate: float




