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
        self.__instruction_info = []
        self.__instruction = []
        print(color_format(">> CPU State:   ", "PURPLE"), end='')
        print(color_format(self.__registers, "PURPLE"))

    def __format_instruction(self):
        byte_groups = []
        byte_group = []
        for byte in self.__instruction:
            byte_group.append(byte)
            if len(byte_group) is self.__arch // 8:
                byte_groups.append(byte_group)
                byte_group = []
        self.__instruction = byte_groups

    def interruption(self, info):
        self.__instruction_info.append(info)
        if len(self.__instruction_info) == 2:
            info_size = self.__instruction_info[0]
            addr = self.__instruction_info[1]
            
            self.__instr_pointer = addr

            self.__bus['control'].send('r')
            self.__bus['data'].send(info_size)
            self.__bus['address'].send(addr)
            self.__instruction_info = []

    def process(self, instr):
        if instr is not 'end':
            self.__instruction.extend(instr)
        else:
            self.__format_instruction()
            decoded_instr = self.__decoder.decode(self.__instruction)
            
            registers_before = self.__registers.copy()
            print(color_format(f'>> Executing:   {instruction_format(decoded_instr)}', "BOLD"))

            operable_instr = self.__operand_conversion(decoded_instr)

            if operable_instr[0] == 'mov':
                self.__mov(operable_instr[1], operable_instr[2])
            elif operable_instr[0] == 'add':
                self.__add(operable_instr[1], operable_instr[2])
            elif operable_instr[0] == 'inc':
                self.__inc(operable_instr[1])
            else:
                self.__imul(operable_instr[1], operable_instr[2], operable_instr[3])

            self.__instruction = []
            if self.__registers != registers_before:
                print(color_format(">> CPU State:   ", "PURPLE"), end='')
                print(color_format(self.__registers, "PURPLE"))

    def __operand_conversion(self, operands):
        mnemonic = operands.pop(0)
        converted_instr = [mnemonic]
        for idx, operand in enumerate(operands):
            if idx is 0: #O primeiro parâmetro sempre é o recipiente da operação
                converted_instr.append(operand)  #Por isso retorna a chave para o recipiente
            else: #Para os outros parâmetros, só são necessários os valores
                if operand in self.__registers: #Registrador
                    converted_instr.append(int(self.__registers[operand]))
                elif operand[:2] == '0x': #RAM
                    converted_instr.append(int(self.__bus['data'].get_ram_value_from(operand)))
                else: #Número
                    converted_instr.append(int(operand))
        return converted_instr
        
    def __mov(self, target_key, value):
        if target_key in self.__registers:
            self.__registers[target_key] = value
        else:
            self.__bus['data'].set_ram_value_at(target_key, value)

    def __add(self, acc_key, addend):
        if acc_key in self.__registers:
            result = self.__registers[acc_key] + addend
            self.__check_for_overflow(result)
            self.__registers[acc_key] = result
        else:
            result = self.__bus['data'].get_ram_value_from(acc_key) + addend
            self.__check_for_overflow(result)
            self.__bus['data'].set_ram_value_at(acc_key, result)

    def __inc(self, target_key):
        if target_key in self.__registers:
            result = self.__registers[target_key] + 1
            self.__check_for_overflow(result)
            self.__registers[target_key] = result
        else:
            result = self.__bus['data'].get_ram_value_from(target_key) + 1
            self.__check_for_overflow(result)
            self.__bus['data'].set_ram_value_at(target_key, result)

    def __imul(self, acc_key, factor1, factor2):
        result = factor1 * factor2
        self.__check_for_overflow(result)

        if acc_key in self.__registers:
            self.__registers[acc_key] = result
        else:
            self.__bus['data'].set_ram_value_at(acc_key, result)

    def __check_for_overflow(self, number):
        if number >= (2 ** self.__arch):
            raise ValueError(color_format('CPU Overflow!!!', "RED"))