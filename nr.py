import sys
args = list(map(lambda x: int(x), sys.argv[1:]))
denom = args[0]
base = args[1]

from modules.non_repeating import tally

print(tally(denom, base))
