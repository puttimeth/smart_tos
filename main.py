from ppadb.client import Client
from mainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
from hotKey import hotkey
import data
from terminalColorize import colorize, Color
import os

def set_working_directory():
    global current_working_directory
    current_working_directory = os.path.dirname(os.path.abspath(__file__))
    print(f'Current working directory: {current_working_directory}')
    os.chdir(current_working_directory)

def get_device():
    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()
    if len(devices) == 0:
        print(colorize('Found no devices.', Color.RED))
        quit()
    print(colorize(f'Found {len(devices)} devices.', Color.GREEN))
    print(colorize(f'Start program on device 0.', Color.GREEN))
    return devices[0]

def main():
    os.system('')
    set_working_directory()
    # get device
    data.device = get_device()
    # hotkey
    hotkey()
    # main app
    app = QApplication([])
    main_window = MainWindow()
    app.exec()

if __name__ == '__main__':
    main()