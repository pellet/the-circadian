import os
import subprocess

def set_night_light_value(value):
    value = max(min(value, 1), 0)
    normalized_value = int(value * 2000 + 1700)
    os.system(f'dconf write /org/gnome/settings-daemon/plugins/color/night-light-temperature "uint32 {normalized_value}"')


if __name__ == '__main__':
    set_night_light_value(1)