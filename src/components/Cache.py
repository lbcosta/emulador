class Cache():
    def __init__(self):
        self.__memory = {}
        # self.__memory['0xfc'] = 0
        # self.__memory['0xfd'] = 1
        # self.__memory['0xfe'] = 4
        # self.__memory['0xff'] = 3

        # print(self.__memory)

    def LFU(self):
        pass

    def insert(self, data):
        self.__memory.update(data)

    def check(self, addr):
        return addr in self.__memory

# cache = Cache()
# result = cache.searchFor([0,1,4,3])
# print(result)


