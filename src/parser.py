import re 
class Parser:
    def parse(self, input_string):
        reg = "[A-Z]" #Registradores = Qualquer letra
        num = "\d+" #Numeros inteiros = Qualquer numero
        mem = "0x\d+" #Espaço de Memoria = 0x(Qualquer numero)
        expressions = [
            f"^(mov)\s+({reg}),\s+({num})$", #mov
            f"^(add)\s+({reg}|{mem}),\s+({reg}|{num})$", #add
            f"^(inc)\s+({reg}|{mem})$", #inc
            f"^(imul)\s+({reg}|{mem}),\s+({reg}|{mem}|{num}),\s+({reg}|{mem}|{num})$" #imul
        ]
        tests = [re.match(expression, input_string) for expression in expressions]
        valid_test = list(filter(lambda test: test != None, tests))
        if(len(valid_test) != 0):
            parameters = valid_test[0].groups()
            return parameters
        else:
            raise SyntaxError('Comando inválido!')
