class Cache():
    def __init__(self):
        self.__memory = {hex(i) : 0 for i in range(0,256)}

    def LFU(self):
        pass

    def fetch(self, target):
        for instruction in self.__memory:
            if instruction is target:
                return instruction
        return 'miss'

