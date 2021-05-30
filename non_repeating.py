#!/usr/local/bin/python
from modules.non_repeating import tally

print('Base 16')
print(48, tally(48, 16))
print(80, tally(80, 16))
print(7, tally(7, 16))
print('Base 8')
print(5, tally(5, 8))
print(4, tally(4, 8))
print(12, tally(12, 8))
print(192, tally(192, 8))
print(96, tally(96, 8))
