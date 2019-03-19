import numpy as np
from Decoder import Decoder
from Register import Register

class CPU():
    def __init__(self, bus, arch):
        self.bus = bus
        self.info = None
        self.arch = arch
        self.decoder = Decoder(arch)
        self.registers = {
            'A': Register('A', None),
            'B': Register('B', None),
            'C': Register('C', None),
            'D': Register('D', None),
        }


    def interruption(self, op, addr, info_size):
        self.bus.read_ram('r', addr, info_size)

    def process(self, info):
        instr = self.decoder.decode(info)
        #mapear operações
        print(f'instrução: {instr}')
