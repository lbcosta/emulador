from helpers.PrintFormat import print_and_sleep
#Erros: arch=16 e bandwidth=8 , arch=64 e bandwidth=32, arch=8 e bandwidth=8
class Bus():
    mode = ''
    
    def __init__(self, arch, bandwidth):
        self.observers = {}
        self.__arch = arch
        self.__bandwidth = bandwidth

    def __if_list_send_in_chunks(self, operation, info):
        if type(info) is list:
            chunk = []
            count = (self.__arch // 8) * len(info)
            for word in info:
                for byte in word:
                    chunk.append(byte)
                    count -= 1
                    if len(chunk) is self.__bandwidth or count is 0:
                        self.observers[operation](chunk)
                        print_and_sleep(chunk)
                        chunk = []
        else:
            self.observers[operation](info)
            print_and_sleep(info)
            

    def send(self, info):
        if info in ['w', 'r', 'i']:
            Bus.mode = info
        else:
            if Bus.mode is 'w':
                self.__if_list_send_in_chunks('RAM_WRITE', info)
            elif Bus.mode is 'r':
                instr = self.observers['RAM_READ'](info)
                print_and_sleep(info)
                if instr is not None:
                    self.__if_list_send_in_chunks('CPU_PROCESS', instr)
                    self.observers['CPU_PROCESS']('end')
                    print_and_sleep('end')
            elif Bus.mode is 'i':
                self.observers['CPU_INTRPT'](info)
                print_and_sleep(info)
            else:
                raise ValueError('Operação de barramento desconhecida')

    def get_ram_pointer(self):
        return self.observers['RAM_PTR']()

    def get_ram_value_from(self, key):
        return self.observers['RAM_GET'](key)

    def set_ram_value_at(self, key, value):
        self.observers['RAM_SET'](key, value)