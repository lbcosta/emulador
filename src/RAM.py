class RAM():
    def __init__(self, bus):
        self.bus = bus
        self.memory = []

    def write(self, op, info, addr, info_size):
        if op == 'w':
            self.memory += info

    def read(self, addr, info_size):
        return self.memory[addr:info_size]