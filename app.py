import json
import sys
from flask import Flask, jsonify

# OUTPUT application/json
def format_payload(data):
	str = json.dumps(data, indent=4, separators=(',', ': '))
	return str, 200, { 'Content-type': 'application/json' }

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route('/pythag/<corner>', methods=['GET'])
def pythag(corner):
	return format_payload(get_pythag())

@app.route('/phi', defaults={'power': 4})
@app.route('/phi/<power>', methods=['GET'])
def phi(power):
	power = int(power)
	#return json.dumps(phi_powers(power), indent=4, separators=(',', ': ')), 200, { 'Content-type': 'application/json'}
	return format_payload(phi_powers(power))

