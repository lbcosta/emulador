class IO():
    def __init__(self, bus):
        self.__bus = bus

    def new_input(self, instr):
        ram_addr = self.__bus.ram_pointer()
        self.__bus.send_instr('w', instr, ram_addr, len(instr))
        self.__bus.send_intrpt('i', ram_addr, len(instr))