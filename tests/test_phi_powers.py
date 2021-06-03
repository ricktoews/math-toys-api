import pytest
import math
from modules.phi import get_phi_power

# Phi: whole numbers, coefficients
def test_phi_1():
    result = get_phi_power(1)
    phi_num = result['phi_num']
    assert phi_num['whole'] == 1 and phi_num['sqrt_5_coef'] == 1

def test_phi_3():
    result = get_phi_power(3)
    phi_num = result['phi_num']
    assert phi_num['whole'] == 4 and phi_num['sqrt_5_coef'] == 2

# Phi: Fibonacci approximations
def test_fibs():
    fibs = []
    # make list of fibonacci numbers 1 - 12.
    for f in range(1, 13):
        result = get_phi_power(f)
        fib = round(result['fib_approx'])
        fibs.append(fib)
    assert fibs == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
