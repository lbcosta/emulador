from time import sleep

class Bus():
    mode = ''
    
    def __init__(self, bandwidth):
        self.observers = {}
        self.__bandwidth = bandwidth

    def __if_list_send_in_chunks(self, operation, info):
        if type(info) is list:
            for x in range(0, len(info), self.__bandwidth):
                chunk = info[x : x + self.__bandwidth]
                print(f'sending chunk {chunk}')
                print('...')
                self.observers[operation](chunk)
                sleep(1)
                print('sent!')
        else:
            self.observers[operation](info)
            sleep(1)
        print('everything sent here :)')
            

    def send(self, info):
        if info in ['w', 'r', 'i']:
            Bus.mode = info
        else:
            if Bus.mode is 'w':
                self.__if_list_send_in_chunks('RAM_WRITE', info)
            elif Bus.mode is 'r':
                instr = self.observers['RAM_READ'](info)
                sleep(1)
                if instr is not None:
                    self.__if_list_send_in_chunks('CPU_PROCESS', instr)
                    self.observers['CPU_PROCESS']('end')
                    sleep(1)
            elif Bus.mode is 'i':
                self.observers['CPU_INTRPT'](info)
                sleep(1)
            else:
                raise ValueError('Operação de barramento desconhecida')

    def get_ram_pointer(self):
        return self.observers['RAM_PTR']()

    def get_ram_value_from(self, key):
        return self.observers['RAM_GET'](key)

    def set_ram_value_at(self, key, value):
        self.observers['RAM_SET'](key, value)