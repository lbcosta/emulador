from components.Emulator import Emulator
from helpers.PrintFormat import color_format
import argparse

argparser = argparse.ArgumentParser(description='Emulador de uma máquina de Von Neumann')
argparser.add_argument('-f', '--file')
argparser.add_argument('-a', '--arch')
args = argparser.parse_args()

if args.arch and args.file:
    emulator = Emulator(args.arch)
    emulator.run(args.file)
else:
    raise ValueError(color_format("Informe o arquivo assembly a ser lido e uma arquiterura", "RED"))
