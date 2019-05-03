import os
from time import sleep

def instruction_format(instr):
    operands = instr[1:]
    instr_str = instr[0] + ' '
    for idx, operand in enumerate(operands):
        if idx == (len(instr) - 2):
            instr_str += str(operand)
        else:
            instr_str += str(operand) + ', '
    return instr_str


def no_empty_format(dictionary):
    d_copy = dictionary.copy()
    for key, value in dict(d_copy).items():
        if value is 0 or isinstance(value, list):
            del d_copy[key]
    return str(d_copy)

def print_and_sleep(data):
    # print(color_format(f'\t\t\t\t{data} sendo enviado...', 'YELLOW'))
    print(color_format(f'\t\t\t\tByte sendo enviado...', 'YELLOW'))
    sleep(1)
    print(color_format('\t\t\t\tEnviado!', 'YELLOW'))


def color_format(content, color_style):
    colors = {
        "PURPLE" : "\033[95m",
        "ORANGE" : "\033[94m",
        "GREEN" : "\033[92m",
        "YELLOW" : "\033[93m",
        "RED" : "\033[91m",
        "ENDC" : "\033[0m",
        "BOLD" : "\033[1m",
        "UNDERLINE" : "\033[4m"
    }

    if os.name == 'posix':
        return colors[color_style] + str(content) + colors["ENDC"]
    else:
        return str(content)
