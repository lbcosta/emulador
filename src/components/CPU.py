from components.Decoder import Decoder
from helpers.PrintFormat import color_format, instruction_format

class CPU():
    def __init__(self, bus, arch):
        self.__bus = bus
        self.__arch = arch
        self.__decoder = Decoder(arch)
        self.__registers = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
        }
        self.__instr_pointer = 0
        
        print(color_format(">> CPU State:   ", "PURPLE"), end='')
        print(color_format(self.__registers, "PURPLE"))


    def interruption(self, op, addr, info_size):
        self.__instr_pointer = addr
        self.__bus.read_ram('r', addr, info_size)

    def process(self, info):
        instr = self.__decoder.decode(info)
        
        print(color_format(f'>> Executing:   {instruction_format(instr)}', "BOLD"))

        operable_instr = [instr.pop(0)] 
        operable_instr += self.__operand_conversion(instr)

        if operable_instr[0] == 'mov':
            self.__mov(operable_instr[1], operable_instr[2])
        elif operable_instr[0] == 'add':
            self.__add(operable_instr[1], operable_instr[2])
        elif operable_instr[0] == 'inc':
            self.__inc(operable_instr[1])
        else:
            self.__imul(operable_instr[1], operable_instr[2], operable_instr[3])

        print(color_format(">> CPU State:   ", "PURPLE"), end='')
        print(color_format(self.__registers, "PURPLE"))

    def __operand_conversion(self, operands):
        converted_operands = []
        for idx, operand in enumerate(operands):
            if idx is 0: #O primeiro parâmetro sempre é o recipiente da operação
                converted_operands.append(operand)  #Por isso retorna a chave para o recipiente
            else: #Para os outros parâmetros, só são necessários os valores
                if operand in self.__registers: #Registrador
                    converted_operands.append(int(self.__registers[operand]))
                elif operand[:2] == '0x': #RAM
                    converted_operands.append(int(self.__bus.get_ram_value_from(operand)))
                else: #Número
                    converted_operands.append(int(operand))
        return converted_operands
        
    def __mov(self, target_key, value):
        if target_key in self.__registers:
            self.__registers[target_key] = value
        else:
            self.__bus.set_ram_value_at(target_key, value)

    def __add(self, acc_key, addend):
        if acc_key in self.__registers:
            self.__registers[acc_key] += addend
        else:
            self.__bus.set_ram_value_at(acc_key, self.__bus.get_ram_value_from(acc_key) + addend)

    def __inc(self, target_key):
        if target_key in self.__registers:
            self.__registers[target_key] += 1
        else:
            self.__bus.set_ram_value_at(target_key, self.__bus.get_ram_value_from(target_key) + 1)

    def __imul(self, acc_key, factor1, factor2):
        if acc_key in self.__registers:
            self.__registers[acc_key] = factor1 * factor2
        else:
            self.__bus.set_ram_value_at(acc_key, factor1 * factor2)