#!/usr/local/bin/python
from modules.tri import nth_triangular
import click

@click.command()
@click.argument('nth')
def nth_tri(nth):
  """ Return the nth triangular number. """
  n = int(nth)
  _tri = nth_triangular(nth)
  click.echo(_tri)

if __name__ == '__main__':
  nth_tri()
