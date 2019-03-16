import re 
class Parser:
    def parse(self, input_string):
        reg = r"[A-Z]" #Registradores = Qualquer letra maiuscula
        num = r"\d+" #Numeros inteiros = Qualquer numero
        mem = r"0[xX][0-9a-fA-F]+" #Espaço de Memoria = 0x(Qualquer numero)
        expressions = [
            rf"^(mov)\s+({reg}),\s+({num})$", #mov
            rf"^(add)\s+({reg}|{mem}),\s+({reg}|{num})$", #add
            rf"^(inc)\s+({reg}|{mem})$", #inc
            rf"^(imul)\s+({reg}|{mem}),\s+({reg}|{mem}|{num}),\s+({reg}|{mem}|{num})$" #imul
        ]
        tests = [re.match(expression, input_string) for expression in expressions]
        valid_test = list(filter(lambda test: test != None, tests))
        if(len(valid_test) != 0):
            parameters = valid_test[0].groups()
            return list(parameters)
        else:
            raise SyntaxError('Comando inválido!')
