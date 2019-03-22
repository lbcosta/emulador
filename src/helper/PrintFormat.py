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

