import sys
from modules.phi import get_phi_power

args = list(map(lambda x: int(x), sys.argv[1:]))
power = args[0]

payload = get_phi_power(power)
print(payload)