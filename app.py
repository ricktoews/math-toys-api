import json
import sys
import os
from flask import Flask, jsonify
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))

from modules.triples_c_minus_b import triples_for_c_minus_b
from modules.triples_c import triples_for_c
from modules.calc_decimal import calc_decimal
from modules.phi import get_phi_power

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
	return format_payload(get_phi_power(power))

@app.route('/phi_list', defaults={'upto': 25})
@app.route('/phi_list/<upto>')
def phi_list(upto):
    upto = int(upto)
    payload = []
    for power in range(1, upto + 1):
        payload.append(get_phi_power(power))
    return format_payload(payload)

if __name__ == "__main__":
    app.run(debug=True)