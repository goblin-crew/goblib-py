from goblib.sec.net.wifi import proberequests as PRQ
from dotenv import dotenv_values
import time

config = dotenv_values('.env')

scanner = PRQ.Scanner(config['IFACE'])

print("start scan")
scanner.scan()