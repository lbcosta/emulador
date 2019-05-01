from components.Parser import Parser
from components.Encoder import Encoder
from components.Bus import Bus
from components.IO import IO
from components.RAM import RAM
from components.CPU import CPU
from helpers.PrintFormat import color_format

class Emulator():
    def __init__(self, arch, bandwidth):
        if int(arch) not in (8, 16, 32, 64):
            raise ValueError(color_format('Arquitetura inválida!',"RED"))
        else:
            self.__arch = int(arch)
            self.__parser = Parser()
            self.__encoder = Encoder(self.__arch)
            self.__bus = {
                'data': Bus(bandwidth),
                'control': Bus(bandwidth),
                'address': Bus(bandwidth)
            }
            self.__io = IO(self.__bus)
            self.__ram = RAM(self.__bus)
            self.__cpu = CPU(self.__bus, self.__arch)

            for key in self.__bus:
                self.__bus[key].observers = {
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

