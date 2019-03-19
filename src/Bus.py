from IO import IO
from RAM import RAM
from CPU import CPU

class Bus():
    def __init__(self):
        self.observers = {}

    def send_instr(self, op, instr, addr, info_size):
        self.observers['RAM_WRITE'](op, instr, addr, info_size)
    
    def send_intrpt(self, op, addr, info_size):
        self.observers['CPU_INTRPT'](op, addr, info_size)

    def read_ram(self, op, addr, info_size):
        info = self.observers['RAM_READ'](addr, info_size)
        self.observers['CPU_PROCESS'](info)

    def ram_pointer(self):
        return self.observers['RAM_PTR']()


