from goblib.general.decorators import validate_args
from goblib.sec.net.wifi.proberequests.exceptions import PacketTypeException

# --------------------------------------------------------------------- #

from scapy.packet import Packet
from scapy.layers import dot11 as d11
import datetime
from datetime import datetime as dt

def args_validator(args: list, kwargs: dict):
    pkt = kwargs["pkt"]
    ts = kwargs["ts"]

    if isinstance(pkt, Packet):
        if not pkt.haslayer(d11.Dot11ProbeReq):
            raise PacketTypeException("Cannot Create ProbeRequest Object --> invalid Packet type")
    else:
        raise TypeError("pkt parameter is not of type [scapy.packet.Packet]")
    
    if not isinstance(ts, datetime.datetime):
        raise TypeError("timestamp-parameter is not of type [datetime.datetime]")

class ProbeRequest:
    '''
    Type Class for Probe-Requests
    '''

    @validate_args(args_validator)
    def __init__(self, pkt: Packet, ts: datetime.datetime = dt.now()) -> None:
        self._packet: Packet = pkt
        self._timestamp: datetime.datetime = ts

        self._ts_str: str = self.timestamp.strftime("%d/%m/%Y | %H:%M:%S")

        self._mac: str = self.packet.addr2
        self._bssid: str = self.mac

        self._ssid: str = self.packet.info

    @property
    def packet(self):
        '''
        read-only property where the probe-request packet is stored
        '''

        return self._packet
    
    @property
    def timestamp(self):
        '''
        read-only property for the timestamp
        '''

        return self._timestamp
    
    @property
    def ts_str(self):
        '''
        read-only property for the string-representation of the timestamp
        '''

        return self._ts_str
    
    @property
    def mac(self):
        '''
        read-only property of the Sender-MAC-Adress
        '''

        return self._mac
    
    @property
    def bssid(self):
        '''
        read-only property of the sender BSSID
        is the same as the MAC-Address
        '''

        return self._bssid
    
    @property
    def ssid(self):
        '''
        read-only property for the SSID that is requested
        '''

        return self._ssid