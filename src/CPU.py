from Decoder import Decoder
from Register import Register

class CPU():
    def __init__(self, bus, arch):
        self.__bus = bus
        self.__arch = arch
        self.__decoder = Decoder(arch)
        self.__registers = {
            'A': Register('A', None),
            'B': Register('B', None),
            'C': Register('C', None),
            'D': Register('D', None),
        }


    def interruption(self, op, addr, info_size):
        self.__bus.read_ram('r', addr, info_size)

    def process(self, info):
        instr = self.__decoder.decode(info)
        #mapear operações
        print(f'instrução: {instr}')
