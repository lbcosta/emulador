from components.Emulator import Emulator
from helpers.PrintFormat import color_format
import argparse

argparser = argparse.ArgumentParser(description='Emulador de uma máquina de Von Neumann')
argparser.add_argument('file', help="Arquivo com código em assemly que deve ser executado")
argparser.add_argument('arch', help="Arquitetura a ser emulada (8, 16, 32, 64)")
args = argparser.parse_args()

if args.arch and args.file:
    emulator = Emulator(args.arch)
    emulator.run(args.file)
    