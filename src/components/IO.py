class IO():
    def __init__(self, bus):
        self.__bus = bus

    def new_input(self, instr):
        ram_addr = self.__bus['address'].get_ram_pointer()
        self.__bus['control'].send('w')
        self.__bus['data'].send(instr)
        self.__bus['data'].send(len(instr))
        self.__bus['address'].send(ram_addr)

        self.__bus['control'].send('i')
        self.__bus['data'].send(len(instr))
        self.__bus['address'].send(ram_addr)