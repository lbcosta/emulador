import re 
class Parser:
    def parse(self, instr):
        regis = r"[A-Z]" #Registradores = Qualquer letra maiuscula
        numbr = r"\d+" #Numeros inteiros = Qualquer numero
        memm = r"0[xX][0-9a-fA-F]+" #Espaço de memoria = 0x(Qualquer numero)
        patterns = [
            rf"^(mov)\s+({regis}),\s+({numbr})$", #mov
            rf"^(add)\s+({regis}|{memm}),\s+({regis}|{numbr})$", #add
            rf"^(inc)\s+({regis}|{memm})$", #inc
            rf"^(imul)\s+({regis}|{memm}),\s+({regis}|{memm}|{numbr}),\s+({regis}|{memm}|{numbr})$" #imul
        ]
        tests = [re.match(expression, instr) for expression in patterns]
        valid_test = list(filter(lambda test: test != None, tests))
        if valid_test:
            parameters = valid_test[0].groups()
            return list(parameters)
        else:
            raise SyntaxError('Comando inválido!')