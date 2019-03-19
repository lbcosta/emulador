import numpy as np
import re
from functools import reduce

class Encoder():
    def __init__(self, arch):
        self.arch = arch

    def get_bytes(self, word):
        mask = np.uint8(0xFF)
        word_bytes = []
        number_of_bytes = self.arch // 8

        for _ in range(0,number_of_bytes):
            byte = np.uint8(word & mask)
            word_bytes.append(byte)
            word = word >> np.uint8(8)

        return word_bytes[::-1]
    
    def encode(self, instr_params):
        opcode = instr_params[0]
        opcode_mapping = {
            'mov': 74,
            'add' : 24,
            'inc' : 4,
            'imul' : 104
        }

        encoded_params = []

        for param in instr_params:
            if param in opcode_mapping:
                encoded_params.append(opcode_mapping[opcode])
            elif param[:2] == '0x':
                encoded_params.append(int(param,16))
            elif re.search('[A-Z]', param):
                encoded_params.append(ord(param))
            else:
                encoded_params.append(int(param))

        byte_groups = []
        for param in encoded_params:
            if self.arch == 8:
                word = np.uint8(param)
            elif self.arch == 16:
                word = np.uint16(param)
            elif self.arch == 32:
                word = np.uint32(param)
            else:
                word = np.uint64(param)
            byte_groups.append(self.get_bytes(word))
        
        return byte_groups
        # return reduce(lambda x, y: x + y, byte_groups)

# DECODER:
# import numpy as np
# num16 = np.uint16(0xAAFF) # = 60000
# lsb = np.uint8(num16 & 0xFF) #Pega o mais significativo
# msb = np.uint8(num16 >> 8) #Pega o menos significativo
# print(f'Palavra: {num16} | Bytes que ocupa: {num16.itemsize}')
# print(f'MSB: {msb} | Bytes que ocupa: {msb.itemsize}')
# print(f'LSB: {lsb} | Bytes que ocupa: {lsb.itemsize}')
# byte_mais_alto = np.uint16(msb) #Guarda byte mais alto em var de 16bits
# print(f'Byte mais alto em 16 bits:{byte_mais_alto}')
# byte_mais_alto_shift = byte_mais_alto << 8 #Shift 8 bits para esquerda
# print(f'Byte mais alto shiftado: {byte_mais_alto_shift}')
# print(f'Soma: {byte_mais_alto_shift | lsb}') #OU com o menos significativo