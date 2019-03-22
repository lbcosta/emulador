import numpy as np

class Decoder():
    def __init__(self, arch):
        self.__arch = arch

    def shift_sum(self, byte_list, conversion_function):
        shifts = (self.__arch // 8) - 1
        definitive_word = conversion_function(0)
        for byte in byte_list:
            word = conversion_function(byte)
            for _ in range(0,shifts):
                word = word << np.uint8(8)
            shifts -= 1
            definitive_word = definitive_word | word
        return definitive_word

    def decode(self, byte_instr):
        opcode_reverse_mapping = {
            74: 'mov',
            24: 'add',
            4 : 'inc',
            104:'imul'
        }

        params = []
        for instr in byte_instr:
            if self.__arch == 8:
                params.append(self.shift_sum(instr, np.uint8))
            elif self.__arch == 16:
                params.append(self.shift_sum(instr, np.uint16))
            elif self.__arch == 32:
                params.append(self.shift_sum(instr, np.uint32))
            else:
                params.append(self.shift_sum(instr, np.uint64))

        conversions = {
            0 : (lambda param: opcode_reverse_mapping[param]),
            1 : (lambda param: chr(param)),
            2 : (lambda param: int(param)),
            3 : (lambda param: hex(param))
        }

        decoded_params = []
        for idx, param in enumerate(params[::-1]):
            if idx % 2 is 0:
                conversion_code = int(param)
            else:
                decoded_params.append(conversions[conversion_code](param))

        return decoded_params[::-1]
