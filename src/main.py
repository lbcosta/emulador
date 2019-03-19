from Parser import Parser
from Encoder import Encoder
from Bus import Bus
from IO import IO
from RAM import RAM
from CPU import CPU

import numpy as np 
arch = 64

parser = Parser()
encoder = Encoder(arch)

instr = "mov A, 2"

params = parser.parse(instr)
encoding = encoder.encode(params)

bus = Bus()
io = IO(bus)
ram = RAM(bus)
cpu = CPU(bus, arch)
bus.observers = {'RAM_WRITE':ram.write,'RAM_READ':ram.read,'CPU_INTRPT':cpu.interruption,'CPU_PROCESS':cpu.process}

io.new_input(encoding)


# print('Decoding:\n')
# for byteArray in encoding:
#     msb = byteArray[0]
#     lsb = byteArray[1]
#     byte_mais_alto = np.uint16(msb) #Guarda byte mais alto em var de 16bits
#     print(f'Byte mais alto em 16 bits:{byte_mais_alto}')
#     byte_mais_alto_shift = byte_mais_alto << 8 #Shift 8 bits para esquerda
#     print(f'Byte mais alto shiftado: {byte_mais_alto_shift}')
#     print(f'Soma: {byte_mais_alto_shift | lsb}') #OU com o menos significativo
