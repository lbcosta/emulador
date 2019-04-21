class Bus():
    mode = ''
    
    def __init__(self):
        self.observers = {}

    def send(self, info):
        if info in ['w', 'r', 'i']:
            Bus.mode = info
        else:
            if Bus.mode is 'w':
                self.observers['RAM_WRITE'](info)
            elif Bus.mode is 'r':
                instr = self.observers['RAM_READ'](info)
                if instr is not None:
                    self.observers['CPU_PROCESS'](instr)
            elif Bus.mode is 'i':
                self.observers['CPU_INTRPT'](info)
            else:
                raise ValueError('Operação de barramento desconhecida')

    def get_ram_pointer(self):
        return self.observers['RAM_PTR']()

    def get_ram_value_from(self, key):
        return self.observers['RAM_GET'](key)

    def set_ram_value_at(self, key, value):
        self.observers['RAM_SET'](key, value)