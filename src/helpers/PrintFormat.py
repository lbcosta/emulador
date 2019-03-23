class PrintFormat():

    @staticmethod
    def format(instr):
        operands = instr[1:]
        instr_str = instr[0] + ' '
        for idx, operand in enumerate(operands):
            if idx == (len(instr) - 2):
                instr_str += str(operand)
            else:
                instr_str += str(operand) + ', '
        return instr_str

    @staticmethod
    def non_empty_dict(dictionary):
        d_copy = dictionary.copy()
        for key, value in dict(d_copy).items():
            if value is 0 or isinstance(value, list):
                del d_copy[key]
        return d_copy


