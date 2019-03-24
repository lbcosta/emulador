import re 
from helpers.PrintFormat import color_format

class Parser:
    def parse(self, instr):
        regis = r"[A-D]" #Registradores = Qualquer letra maiuscula
        numbr = r"\d+" #Numeros inteiros = Qualquer numero
        #O espaço de memória da RAM é dividido em instruções (de 0x0 a 0x7fff) e dados (0x8000 a 0xffff)
        memm = r"0x[89a-f][0-9a-f]{3}" #Ou seja, nada abaixo de 0x8000 é válido em uma instrução

        patterns = [
            rf"^(mov)\s+({regis}|{memm}),\s+({regis}|{numbr})$", #mov
            rf"^(add)\s+({regis}|{memm}),\s+({regis}|{numbr})$", #add
            rf"^(inc)\s+({regis}|{memm})$", #inc
            rf"^(imul)\s+({regis}|{memm}),\s+({regis}|{memm}|{numbr}),\s+({regis}|{memm}|{numbr})$" #imul
        ]

        tests = [re.match(pattern, instr) for pattern in patterns]
        valid_test = list(filter(lambda test: test != None, tests))

        if valid_test:
            parameters = valid_test[0].groups()
            return list(parameters)
        else:
            raise SyntaxError(color_format('Instrução inválida! Cheque sua sintaxe ou se o espaço de memória é permitido', "RED"))
