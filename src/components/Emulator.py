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
        if bandwidth not in (8, 16, 32, 64):
            raise ValueError(color_format('Largura de banda inválida!',"RED"))
        else:
            self.__arch = int(arch)
            self.__bandwidth = bandwidth
            self.__parser = Parser()
            self.__encoder = Encoder(self.__arch)
            self.__bus = {
                'data': Bus(self.__arch, bandwidth),
                'control': Bus(self.__arch, bandwidth),
                'address': Bus(self.__arch, bandwidth)
            }
            self.__io = IO(self.__bus)
            self.__ram = RAM(self.__bus, self.__arch)
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
        print()
        print(color_format('**********', 'BOLD'))
        print(color_format(f'Arquivo: {assembly_file}', 'BOLD'))
        print(color_format(f'Tamanho da palavra: {self.__arch} bits', 'BOLD'))
        print(color_format(f'Clock: {self.__bandwidth} bytes/segundo', 'BOLD'))
        print(color_format('**********', 'BOLD'), end='\n\n')
        self.__cpu.print_state()
        self.__ram.print_state()
        with open(assembly_file, 'r') as assembly_code:
            for line in assembly_code:
                parsed_instr = self.__parser.parse(line.rstrip())
                encoded_instr = self.__encoder.encode(parsed_instr)
                self.__io.new_input(encoded_instr)

