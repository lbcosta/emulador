from parser import Parser
from encoder import Encoder

arch = 16

parser = Parser()
encoder = Encoder(arch)

instr = "add 0x00A, 17"

params = parser.parse(instr)
encoding = encoder.encode(params)
print(encoding)