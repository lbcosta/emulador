from Emulator import Emulator

ARCH = 16
FILE = "../assembly.txt"

emulator = Emulator(ARCH)
emulator.run(FILE)