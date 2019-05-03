from helpers.PrintFormat import no_empty_format, color_format

class RAM():
    def __init__(self, bus, arch):
        self.__bus = bus
        self.__arch = arch
        self.__pointer = '0x0'
        self.__memory = {hex(i) : 0 for i in range(0,65536)}
        self.__instruction = []
        print(color_format(">> RAM State:   ", "ORANGE"), end='')
        print(color_format(no_empty_format(self.__memory), "ORANGE"))

    def __format_instruction(self):
        byte_list = []
        for byte in self.__instruction[0]:
            byte_list.append(byte)
        byte_groups = []
        byte_group = []
        for byte in byte_list:
            byte_group.append(byte)
            if len(byte_group) is self.__arch // 8:
                byte_groups.append(byte_group)
                byte_group = []
        self.__instruction[0] = byte_groups


    def write(self, info):
        if type(info) is list:
            try:
                self.__instruction[0].extend(info)
            except: #Se for o primeiro chunk, inicia uma nova lista na posição 0.
                self.__instruction.append(info)
        else:
            self.__instruction.append(info)
            if len(self.__instruction) == 3:
                self.__format_instruction()
                instr = self.__instruction[0]
                for param in instr:
                    self.__memory[self.__pointer] = param
                    self.__pointer = hex(int(self.__pointer, 16) + 1)
                if int(self.__pointer, 16) >= (len(self.__memory) // 2):
                    raise ValueError(color_format("RAM Overflow!!!", "RED"))
                self.__instruction = []

    def read(self, info):
        self.__instruction.append(info)
        if len(self.__instruction) == 2:
            instr = []
            info_size = self.__instruction[0]
            addr = self.__instruction[1]

            for pos in range(0,info_size):
                relative_addr = self.__memory[hex(int(addr, 16) + pos)]
                instr.append(relative_addr)
                
            self.__instruction = []
            return instr
        else:
            return None

    def get_value(self, key):
        return self.__memory[key]

    def set_value(self, key, value):
        self.__memory[key] = value
        print(color_format(">> RAM State:   ", "ORANGE"), end='')
        print(color_format(no_empty_format(self.__memory), "ORANGE"))

    def pointer(self):
        return self.__pointer
