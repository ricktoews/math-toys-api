#!/usr/local/bin/python
import sys

from modules.calc_decimal import calc_decimal

args = sys.argv[1:]
num = int(args[0])
denom = int(args[1])
base = int(args[2])

print(f'for {num}/{denom}, base {base}:')
print(calc_decimal(num, denom, base))
