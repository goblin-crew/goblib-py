from goblib.sec.net.wifi import proberequests as PRQ
from dotenv import dotenv_values
import time

config = dotenv_values('.env')

scanner = PRQ.Scanner(config['IFACE'])

print("start scan")

try:
    scanner.scan()
except KeyboardInterrupt:
    scanner.wifi_iface.set_mode_managed()

print("results")

for i in scanner.data:
    print(f"{i.mac}\t->\t{i.ssid}")