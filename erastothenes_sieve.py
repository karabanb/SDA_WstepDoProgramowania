

def erastothenes_sieve(n):

    """ This function returns primary numbers which are less tnan n """

    if not n > 1:
        print('Bad data@')
        return
    sieve = []
    for i in range(n):
           sieve.append(True)
    for i in range(2, n // 2):
        if sieve[i]:
            for j in range(2 * i, n, i):
                sieve[j] = False
        result_list = []
    for i in range(2, n):
        if sieve[i]:
                result_list.append(i)
    return result_list


if __name__ == "__main__":
    prime_numbers = erastothenes_sieve(100)
    print(prime_numbers)


# przekazywanie wartosci przez obiekt

def append_a(my_list):
    my_list.append('a')

some_list = []
append_a(some_list)
print(some_list)


def assign(my_list):
    my_list =['a']

some_list2 = ['b', 'a']
assign(some_list2)
print(some_list)

# Typing

# Funkcja jest obiektem


def get_discounted_price(price, discount_func):
    return discount_func(price)


def discount_func_1(price):
    return 0.8 * price


def discount_func_2(price):
    return 0.9 * price - 1

print(get_discounted_price(99, discount_func_1()))
print(get_discounted_price(99, discount_func_2()))