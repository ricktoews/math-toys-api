import click
import urllib.request
import json

def getData(api, param):
  res = urllib.request.urlopen(API[api] + param).read()
  res = str(res, 'utf-8')
  data = json.loads(res)
  return data

API = {
  'dc': 'http://arithmo-rest.toewsweb.net/dc/'
}

@click.command()
@click.argument('denom')
def dc(denom):
  data = getData('dc', denom)
  first = data[0]
  (fraction, decimal, length, repeating) = [first[k] for k in ('fraction', 'decimal', 'length', 'repeating')]

  click.echo('Fraction: %s, Decimal: %s, Length: %s, Repeating: %s' % (fraction, decimal, length, repeating))


if __name__ == '__main__':
  dc()
