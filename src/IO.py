class IO():
    def __init__(self, bus):
        self.bus = bus

    def new_input(self, instr):
        ram_addr = 0
        self.bus.send_instr('w', instr, ram_addr, len(instr))
        self.bus.send_intrpt('i', ram_addr, len(instr))