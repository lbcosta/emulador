import numpy as np
import re

class Encoder():
    def __init__(self, arch):
        self.__arch = arch

    def get_bytes(self, word):
        mask = np.uint8(0xFF)
        word_bytes = []
        number_of_bytes = self.__arch // 8

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
            'imul' : 104,
            'jmp' : 73,
            'lbl' : 103
        }

        encoded_params = []

        for param in instr_params:
            if param in opcode_mapping:
                encoded_params.append(opcode_mapping[opcode])
                encoded_params.append(0)
            elif param[:2] == '0x':
                encoded_params.append(int(param,16))
                encoded_params.append(3)
            elif re.search('[A-D<>=]', param):
                encoded_params.append(ord(param))
                encoded_params.append(1)
            else:
                encoded_params.append(int(param))
                encoded_params.append(2)

        byte_groups = []
        for param in encoded_params:
            if self.__arch == 8:
                word = np.uint8(param)
            elif self.__arch == 16:
                word = np.uint16(param)
            elif self.__arch == 32:
                word = np.uint32(param)
            else:
                word = np.uint64(param)
            byte_groups.append(self.get_bytes(word))
        
        return byte_groups
        