from Emulator import Emulator

ARCH = 16
FILE = "../code.asm"

emulator = Emulator(ARCH)
emulator.run(FILE)