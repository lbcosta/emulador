from Decoder import Decoder
from helpers.PrintFormat import PrintFormat

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
        
        print(f'>> State:       {self.__registers}')


    def interruption(self, op, addr, info_size):
        self.__instr_pointer = addr
        self.__bus.read_ram('r', addr, info_size)

    def process(self, info):
        instr = self.__decoder.decode(info)

        print(f'>> Executing:   {PrintFormat.format(instr)}')
        
        if instr[0] == 'mov':
            self.__mov(instr[1], instr[2])
        elif instr[0] == 'add':
            self.__add(instr[1], instr[2])
        elif instr[0] == 'inc':
            self.__inc(instr[1])
        else:
            self.__imul(instr[1], instr[2], instr[3])

        print(f'>> State:       {self.__registers}')

    def __mov(self, target_key, value):
        if value in self.__registers:
            self.__registers[target_key] = self.__registers[value]
        else:
            self.__registers[target_key] = value

    def __add(self, acc_key, addend):
        if addend in self.__registers:
            self.__registers[acc_key] += self.__registers[addend]
        else:
            self.__registers[acc_key] += addend

    def __inc(self, target):
        if self.__registers[target] is None:    
            self.__registers[target] = 1
        else:
            self.__registers[target] += 1


    def __imul(self, acc_key, factor1, factor2):
        if factor1 in self.__registers:
            if factor2 in self.__registers:
                self.__registers[acc_key] = self.__registers[factor1] * self.__registers[factor2]
            else:
                self.__registers[acc_key] = self.__registers[factor1] * factor2
        else:
            if factor2 in self.__registers:
                self.__registers[acc_key] = factor1 * self.__registers[factor2]
            else:
                self.__registers[acc_key] = factor1 * factor2