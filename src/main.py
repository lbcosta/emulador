from parser import Parser
from encoder import Encoder
import numpy as np 
arch = 16

parser = Parser()
encoder = Encoder(arch)

instr = "add 0x111, 280"

params = parser.parse(instr)
encoding = encoder.encode(params)
print(encoding)
print('Decoding:\n')
for byteArray in encoding:
    msb = byteArray[0]
    lsb = byteArray[1]
    byte_mais_alto = np.uint16(msb) #Guarda byte mais alto em var de 16bits
    print(f'Byte mais alto em 16 bits:{byte_mais_alto}')
    byte_mais_alto_shift = byte_mais_alto << 8 #Shift 8 bits para esquerda
    print(f'Byte mais alto shiftado: {byte_mais_alto_shift}')
    print(f'Soma: {byte_mais_alto_shift | lsb}') #OU com o menos significativo
