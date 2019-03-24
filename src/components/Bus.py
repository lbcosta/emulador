class Bus():
    def __init__(self):
        self.observers = {}

    def send_operation(self, op, addr, instr_size, instr=''):
        if op is 'w':
            self.observers['RAM_WRITE'](instr, addr, instr_size)
        elif op is 'r':
            instr = self.observers['RAM_READ'](addr, instr_size)
            self.observers['CPU_PROCESS'](instr)
        elif op is 'i':
            self.observers['CPU_INTRPT'](addr, instr_size)
        else:
            raise ValueError('Operação inválida')
    
    def get_ram_pointer(self):
        return self.observers['RAM_PTR']()

    def get_ram_value_from(self, key):
        return self.observers['RAM_GET'](key)

    def set_ram_value_at(self, key, value):
        self.observers['RAM_SET'](key, value)



