class RAM():
    def __init__(self, bus):
        self.__bus = bus
        self.__pointer = '0x0'
        self.__memory = {hex(i) : [] for i in range(0,256)}

    def write(self, op, instr, addr, info_size):
        if op == 'w':
            for param in instr:
                self.__memory[self.__pointer] = param
                self.__pointer = hex(int(self.__pointer, 16) + 1)

    def read(self, addr, info_size):
        instr = []
        for pos in range(0,info_size):
            relative_addr = self.__memory[hex(int(addr, 16) + pos)]
            instr.append(relative_addr)
        return instr

    def get_value(self, key):
        return self.__memory[key]

    def set_value(self, key, value):
        self.__memory[key] = value

    def pointer(self):
        return self.__pointer
