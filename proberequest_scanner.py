from goblib.sec.net.wifi.proberequests.utils import WifiInterface
from scapy.all import *
import datetime


a=[]
# Opening a list to adjuest SSID
def probes_scanner(packet):
	if packet.haslayer(Dot11ProbeReq):
		t=datetime.datetime.today()
		a.append(packet.info)
		print( ' ' + str(len(a))+'.' +'   '  +'['+ str(t)+']' + '  SSID: '+  packet.info+  '   ' 
			+ ' BSSID: ' +packet.addr2)

wifi_iface = WifiInterface("wlp0s20f3")
wifi_iface.set_mode_monitor()

try:
    #s = sniff(iface="wlp0s20f3", prn=probes_scanner, count=0)
	s = sniff(prn=probes_scanner, count=0)
except KeyboardInterrupt:
	wifi_iface.set_mode_managed()

wifi_iface.set_mode_managed()
print(wifi_iface.in_managed_mode)
print(s.summary())
print(a)