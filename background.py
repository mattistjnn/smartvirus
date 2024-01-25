import ctypes
import os
import requests

SPI_SETDESKWALLPAPER = 0x0014

def change_wallpaper(file_path):
    file_path = os.path.abspath(file_path)
    file_path = file_path.encode('utf-16le') + b'\x00\x00'
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, 3)

if __name__ == "__main__":
    local_path = './chocoblast.png'
    change_wallpaper(local_path)
