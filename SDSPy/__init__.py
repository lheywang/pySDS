# Aux files !
# Others files
from .acquisition import SiglentAcquisition
from .channel import SiglentChannel
from .communication import SiglentCommunication
from .cursor import SiglentCursor
from .decode import SiglentDecode
from .deprecated_functions import ACAL, DATE, COUNTER
from .digital import SiglentDigital
from .display import SiglentScreen
from .Files import SiglentFiles
from .generics import SCPIGenerics
from .history import SiglentHistory
from .maths import SiglentMaths
from .measure import SiglentMeasure
from .passfail import SiglentPassFail
from .references import SiglentReference
from .timebase import SiglentTimebase
from .trigger import SiglentTrigger
from .waveform import SiglentWaveform

# Main init.py file !
from .pySDS import PySDS