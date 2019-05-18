
import math

# funkcje wbudowane

print('a')
print(type(str(1)))

# import modułów biblioteki standardowej

num_pi = math.pi
print(num_pi)

# import wybranej funkcji z modułu

from math import pi

num_pi2 = pi

a = 4


def function_scope_1():
    a = 90
    print(a)


if __name__ == 'main':
    function_scope_1()
    print(a)


# import z modułu (innego pliku)

from erastothenes_sieve import erastothenes_sieve

prime_number = erastothenes_sieve(100)
print(prime_number)

