class IO():
    def __init__(self, bus):
        self.__bus = bus

    def new_input(self, instr):
        ram_addr = self.__bus.get_ram_pointer()
        self.__bus.send_operation('w', ram_addr, len(instr), instr)
        self.__bus.send_operation('i', ram_addr, len(instr))