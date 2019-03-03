import numpy as np
import re
class Encoder():
    def __init__(self, arch):
        self.arch = arch

    def conversion(self, param):
        param_bin = np.binary_repr(param).zfill(self.arch)
        lista_de_bytes = self.byte_chunks(param_bin)
        lista_de_bytes = [np.uint8(byte) for byte in lista_de_bytes]
        return lista_de_bytes


    def byte_chunks(self, bin_str):
        for i in range(0, len(bin_str), 8):
            yield bin_str[i:i + 8]


    def encode(self, params):
        opcode = params[0]
        opcode_mapping = {
            'mov': 74,
            'add' : 24,
            'inc' : 4,
            'imul' : 104
        }

        for idx, param in enumerate(params):
            if param in opcode_mapping:
                params[0] = opcode_mapping[opcode]
            elif param[:2] == '0x':
                params[idx] = int(param,16)
            elif re.search('[A-Z]', param):
                params[idx] = ord(param)
            else:
                params[idx] = int(param)
            params[idx] = self.conversion(params[idx])

        
        return params

            # if self.arch == 8:
            #     param_bin = np.binary_repr(param).zfill(8)
            #     return [np.uint8(param) for param in params]
            # elif self.arch == 16:
            #     param_bin = np.binary_repr(param).zfill(16)
            #     return [np.uint16(param) for param in params]
            # elif self.arch == 32:
            #     param_bin = np.binary_repr(param).zfill(32)
            #     return [np.uint32(param) for param in params]
            # else:
            #     param_bin = np.binary_repr(param).zfill(64)
            #     return [np.uint64(param) for param in params]

