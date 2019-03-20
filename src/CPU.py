from Decoder import Decoder

class CPU():
    def __init__(self, bus, arch):
        self.__bus = bus
        self.__arch = arch
        self.__decoder = Decoder(arch)
        self.__registers = {
            'A': None,
            'B': None,
            'C': None,
            'D': None,
        }
        self.__instr_pointer = None
        print(f'>> {self.__registers}')


    def interruption(self, op, addr, info_size):
        self.__instr_pointer = addr
        self.__bus.read_ram('r', addr, info_size)

    def process(self, info):
        instr = self.__decoder.decode(info)

        #TODO: TRATAMENTO DAS OUTRAS OPERAÇÕES ALÉM DO "MOV REG, NUM"
        print(f'>> {instr[0]} {instr[1]}, {instr[2]}')
        self.__mov(instr[1], instr[2])
        print(f'>> {self.__registers}')

    def __mov(self, target_key, value):
        self.__registers[target_key] = value

    def __add(self, acc_key, addend):
        pass

    def __inc(self, target):
        pass

    def __imul(self, acc, factor1, factor2):
        pass