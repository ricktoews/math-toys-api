import sys
args = list(map(lambda x: int(x), sys.argv[1:]))
num = args[0]
denom = args[1]
base = args[2]

from modules.calc_decimal import calc_decimal

print(calc_decimal(num, denom, base))