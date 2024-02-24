import os
import re as regex
from typing import Any, Self
import subprocess

def shell(cmd: str):
    try:        
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output}"

class WifiInterface:
    def __init__(self, name: str) -> None:
        if os.name != "posix":
            raise RuntimeError("Module is currently only available for Linux systems!!!")
        else:
            self.name = name
            self.__install_apt_packages__('net-tools', 'wireless-tools')


    def __install_apt_packages__(self, *args):
        return shell(f"apt install -y {' '.join(args)}")

    def __set_to_status__(self, up: bool):
        return shell(f"ifconfig {self.name} {'up' if up else 'down'}")

    def __set_to_mode__(self, mode: str):
        return shell(f"iwconfig {self.name} mode {mode}")
    
    def __get_status__(self) -> str:
        output = shell(f"iwconfig {self.name}")

        status_match = regex.search(r"Status:(\S+)", output)
        if status_match:
            status = status_match.group(1)
            return status
        else:
            return "Error: Unable to extract status from iwconfig output."

    def __get_mode__(self):
        output = shell(f"iwconfig {self.name}")

        mode_match = regex.search(r"Mode:(\S+)", output)
        if mode_match:
            mode = mode_match.group(1)
            return mode
        else:
            return "Error: Unable to extract mode from iwconfig output."

    def set_mode_monitor(self) -> Self:
        self.set_down()
        self.__set_to_mode__("monitor")
        self.set_up()
        return self
    
    def set_mode_managed(self) -> Self:
        self.set_down()
        self.__set_to_mode__("managed")
        self.set_up()
        return self
    
    def set_up(self) -> Self:
        self.__set_to_status__(True)
        return self
    
    def set_down(self) -> Self:
        self.__set_to_status__(False)
        return self

    @property
    def up(self) -> bool:
        return bool(regex.match('^[Uu][Pp]$', self.__get_status__()) != None)

    @property
    def down(self) -> bool:
        return bool(regex.match('^[Dd][Oo][Ww][Nn]$', self.__get_status__()) != None)

    @property
    def in_managed_mode(self) -> bool:
        return bool(regex.match('^[Mm][Aa][Nn][Aa][Gg][Ee][Dd]$', self.__get_mode__()) != None)

    @property
    def in_monitor_mode(self) -> bool:
        return bool(regex.match('^[Mm][Oo][Nn][Ii][Tt][Oo][Rr]$', self.__get_mode__()) != None)