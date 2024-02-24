from goblib.general.decorators import validate_args
from goblib.general.errors import *
from goblib.sec.net.wifi.probe_requests.errors import *
from goblib.sec.net.wifi.probe_requests.utils import *

# --------------------------------------------------------------------- #

from scapy.packet import Packet
from scapy.layers import dot11 as d11
import datetime
from datetime import datetime as dt

def args_validator(args: list, kwargs: dict):
    pkt = kwargs["pkt"]
    ts = kwargs["ts"]

class ProbeRequest:
    @validate_args(args_validator)
    def __init__(self, pkt: Packet, ts: datetime.datetime = dt.now()) -> None:
        pass