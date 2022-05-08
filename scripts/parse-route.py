import re

routes = [
'/phi/:power', 
'/tri/:n',
'/dc/:denom/:num'
]

param_re = re.compile(':(\w+)')
for rpattern in routes:
    route = param_re.sub('w+', rpattern)
    var = re.group(0)
    print(rpattern, var, route)
