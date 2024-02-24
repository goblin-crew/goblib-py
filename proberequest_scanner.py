from goblib.sec.net.wifi import proberequests as PRQ
from dotenv import dotenv_values
import time

config = dotenv_values('.env')

scanner = PRQ.Scanner(config['IFACE'])

print("start scanner....")
scanner.start()

t = 0
while not scanner.started:
    print(f"\rwaiting for scanner start... ({t}s)", end='')
    time.sleep(0.5)
    t += 0.5

print()

for i in range(0, 120):
    print(f"\rscanning ({i}s)", end='')
    time.sleep(1)

print()

print("time elapsed")
print("stopping scanner....")
scanner.stop(True)
print("scanner stopped!")

print("scanner results:")

for i in scanner.data:
    print(f"{i.timestamp}\t[{i.mac}]\t{i.ssid}")

print("\n")