import numpy as np
import re

class ES():
    def input(self, escrita, instrucao, tam, endereco):
        if(escrita):
            print('operação de escrita')
        else:
            print('operação de leitura')

    def buffer(self):
        print('envia pro buffer')

    def output(self):
        print('envia para RAM')