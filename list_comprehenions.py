
naturals = []

for i in range(100):
    naturals.append(i)
print(naturals)

naturals_c = [i for i in range(100)]
print(naturals_c)

# stare zadanie z konwersja liczb


def get_numbers_to_str_old():
    d={}
    for i in range(10):
        d[i] = str(i)
    print(d)


def def_get_number_to_str():
    return{i: str(i) for i in range(10)}


def number_to_any_base(number, base):
    numbers_to_str = def_get_number_to_str()
    hex_numbers = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    numbers_to_str.update(hex_numbers)
    result_list =[]
    while number > 0:
        rest = number % base
        str_representation = numbers_to_str[rest]
        result_list.append(str_representation)
        number //= base
    result_list.reverse()
    return ''.join(result_list)