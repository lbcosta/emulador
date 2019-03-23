import re 
from helpers.PrintFormat import color_format

class Parser:
    def parse(self, instr):
        regis = r"[A-D]" #Registradores = Qualquer letra maiuscula
        numbr = r"\d+" #Numeros inteiros = Qualquer numero
        memm = r"0x[0-9a-f]{,2}" #Espaço de memoria = 0x(Qualquer numero de 00 a ff)

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
            raise SyntaxError(color_format('Instrução inválida!', "RED"))
