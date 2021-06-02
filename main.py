import json
import sys
import os
from flask import Flask, jsonify
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))

from modules.triples_c_minus_b import triples_for_c_minus_b
from modules.triples_c import triples_for_c
from modules.calc_decimal import calc_decimal

# OUTPUT application/json
def format_payload(data):
	str = json.dumps(data, indent=4, separators=(',', ': '))
	return str, 200, { 'Content-type': 'application/json' }

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

# Pythagorean triples for c - b
# Payload is list of triples, with prime flag for each.
@app.route('/pythag/<c_minus_b>', methods=['GET'])
def pythag(c_minus_b):
	return format_payload(triples_for_c_minus_b(int(c_minus_b)))

# Pythagorean triples for optionally specified values of c.
# Payload is list of triples, with prime flag for each.
@app.route('/pythag-c', defaults={'c':''}, methods=['GET'])
@app.route('/pythag-c/<c>', methods=['GET'])
def pythag_c(c):
    print('pythag_c; c:', c)
    if c == '':
        # if c not specified, use arbitrary range [5..500]
        c_list = range(5,500)
    else :
        # allow comma-delimited list of values in the URL
        c_list = list(map(lambda x: int(x), c.split(',')))
    return format_payload(triples_for_c(c_list))

# Decimal Calculator.
# Accepts denominator and optional numerator and base.
# Response payload includes decimal expansion period, tallies of repeating and non-repeating digits.
@app.route('/dc/<denom>', defaults={'num': 1, 'base': 10})
@app.route('/dc/<denom>/<num>', defaults={'base': 10})
@app.route('/dc/<denom>/<num>/<base>')
def dc(denom, num, base):
    denom = int(denom)
    num = int(num)
    base = int(base)
    payload = calc_decimal(num, denom, base)
    return format_payload(payload)

@app.route('/phi', defaults={'power': 4})
@app.route('/phi/<power>', methods=['GET'])
def phi(power):
	power = int(power)
	#return json.dumps(phi_powers(power), indent=4, separators=(',', ': ')), 200, { 'Content-type': 'application/json'}
	return format_payload(phi_powers(power))

if __name__ == "__main__":
    app.run(debug=True)