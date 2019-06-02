class Cache():
    def __init__(self):
        self.__memory = {}
        self.__label_map = {}

    def LFU(self):
        pass

    @property
    def memory(self):
        return self.__memory

    def instruction_at(self, key):
        return self.__memory[key]

    def push(self, data):
        self.__memory.update(data)

    def check(self, addr):
        return addr in self.__label_map

    def map_label_to_addr(self, label, addr):
        self.__label_map[label] = addr

    def get_addr_on(self, label):
        return self.__label_map[label]