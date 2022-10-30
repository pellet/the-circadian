import os
import subprocess
from sys import platform

def set_night_light_value_linux(value):
    value = max(min(value, 1), 0)
    normalized_value = int(value * 2000 + 1700)
    os.system(f'dconf write /org/gnome/settings-daemon/plugins/color/night-light-temperature "uint32 {normalized_value}"')

def set_night_light_value_mac(value):
    value = max(min(value, 1), 0)
    normalized_value = int(value * 100)
    os.system(f'nightlight temp {normalized_value}')

def set_night_light_value_windows(value):
    print("the circadian not implemented yet for windows.")

def set_night_light_value(value):
    if platform == "linux" or platform == "linux2":
        # linux
        set_night_light_value_linux(value)
    elif platform == "darwin":
        # OS X
        set_night_light_value_mac(value)
    elif platform == "win32":
        # Windows...
        set_night_light_value_windows(value)

if __name__ == '__main__':
    set_night_light_value(1)