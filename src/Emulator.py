from Parser import Parser
from Encoder import Encoder
from Bus import Bus
from IO import IO
from RAM import RAM
from CPU import CPU

class Emulator():
    def __init__(self, arch):
        if arch not in (8, 16, 32, 64):
            raise ValueError('Arquitetura inválida!')
        else:
            self.__arch = arch
            self.__parser = Parser()
            self.__encoder = Encoder(self.__arch)
            self.__bus = Bus()
            self.__io = IO(self.__bus)
            self.__ram = RAM(self.__bus)
            self.__cpu = CPU(self.__bus, self.__arch)

            self.__bus.observers = {
                'RAM_WRITE':self.__ram.write,
                'RAM_READ':self.__ram.read,
                'RAM_PTR': self.__ram.pointer,
                'RAM_GET': self.__ram.get_value,
                'RAM_SET': self.__ram.set_value,
                'CPU_INTRPT':self.__cpu.interruption,
                'CPU_PROCESS':self.__cpu.process
            }

    def run(self, assembly_file):
        with open(assembly_file, 'r') as assembly_code:
            for line in assembly_code:
                parsed_instr = self.__parser.parse(line.rstrip())
                encoded_instr = self.__encoder.encode(parsed_instr)
                self.__io.new_input(encoded_instr)

