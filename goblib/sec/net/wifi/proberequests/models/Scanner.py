from scapy.packet import Packet
from scapy.layers import dot11 as d11
from scapy.sendrecv import sniff

from goblib.sec.net.wifi.proberequests.models import ProbeRequest
from goblib.sec.net.wifi.proberequests.utils import WifiInterface

from typing_extensions import Self

class Scanner:
    '''
    A Wifi-ProbeRequest-Scanner \n
    uses scapy.sendrecv.AsyncSniffer with preconfigured values and results return as ProbeRequest-Objects \n


    @property data          <list[ProbeRequest]>            collected ProbeRequest-Packets during scan
    @property __sniffer__   <scapy.sendrecv.AsyncSniffer>   internal obj for sniffing
    @property quiet         <bool>                          defines if the captured packets are printed during scan
    @property running       <bool>                          is true when scan thread is running

    @param iface            <string>                        name of the Wifi-Interface in monitoring mode
    @param count            <int>                           how many packets are sniffed | default: 0 --> infinite sniffing
    @param quiet            <bool>                          if the captured packets should be printed during scan | default: false
    @param ignore_sniffer_errors <bool>                     if errors in the sniffer should be suppressed | default: false
    '''
    def __init__(self, iface: str, count: int = 0, quiet: bool = False, ignore_sniffer_errors: bool = False) -> None:
        self.data: list[ProbeRequest] = []
        self.quiet: bool = quiet
        self.wifi_iface = WifiInterface(iface)
        self.stop: bool = False

        self.__config__: dict = {
            'iface': iface,
            'count': count,
            'quiet': ignore_sniffer_errors
        }
        

    def __handle_packet__(self, pkt: Packet):
        if isinstance(pkt, Packet):
            if pkt.haslayer(d11.Dot11ProbeReq):
                prq = ProbeRequest(pkt=pkt)
                self.data += [prq]

                if not self.quiet:
                    print(f"({prq.ts_str})\t[{prq.mac}]\t{prq.ssid}")
    
    def scan(self) -> Self:
        if self.wifi_iface.in_managed_mode:
            self.wifi_iface.set_mode_monitor()

        sniff(iface=self.__config__['iface'], count=self.__config__['count'], store=True, prn=self.__handle_packet__, monitor=True, quiet=self.__config__['quiet'])
        return self