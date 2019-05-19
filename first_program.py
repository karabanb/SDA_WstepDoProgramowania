if __name__ == "__main__":
    print('Hello, World!')
    # to jest komentarz
    # zakomentowana instrukcja się nie wykona

my_name = 'Bartek'
my_surname = 'Karaban'
my_height = 181
my_age = 37

print(my_name)
print(my_age)

my_age = my_age - 5
print(my_age)

a = 22
b = 0b10110
c = 0o27
d = 0x22A

# napisy i zmienne

name = 'Aleks'
print(f'Hello, {name}')  # konstrukcja fstring
print(name)

# sprawdzanie typu zmiennej

x = 14
x = 'qwerty'

type(x)

# sprawdzenie obiektu w pamięci - zmienne to etykiety

a = 42
b = 42

id(a)
id(b)  # sa to te same obikety ale o innej etykiecie

b = b + 1

id(a)
id(b)

# instrukcja input

name = input('Podaj swoje imie: ')
surname = input('Podaj swoje nazwisko: ')

print(f'Witaj {name} {surname}!')

age = input('Podaj swój wiek: ')
age = int(age) + 1

print(f'Za rok będziesz mieć {age} lat.')

a = 43

if a < 42:
    print('jest mniejsza niz 42')
elif a == 42:
    print('to jest liczba 42')
else:
    print('jest większe niż 42')

a = 124

if a > 100 and a % 4 == 0:
    print(a)


# funckje

def add(x1, x2):
    print(x1 + x2)  # zwraca None, nie można przypisać do zmiennej


def add_ret(x, y):  # można zapisać do zmiennej
    return x + y


def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False


def is_odd_better(number):
    if number % 2 != 0:
        return True
    return False


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def nieuzywana_chujnia():
    pass  # pass - pycharm nie krzyczy, ze funkcja nic nie robi, kod przejdzie dalej


# Petla while

number = 0

while number < 7:
    print(number)
    number += 1

number = 7

while number < 7:  # infinity loop
    print(number)

while True:
    print('It\'s very infinite loop')  # infinity loop

counter = 0

while counter < 100:
    counter += 1
    if counter == 4:
        print('I do not like 4. Continue')
        continue
    print(f'My numer is: {counter}')
    if counter == 9:
        print('9 it is enough. Break')
        break
    print('\tend')

'''
Napiszemy program który konwertuje liczbe dziesiętną na binarną
'''


def dec_to_bin(n):
    while n > 0:
        print(n % 2)
        n = n // 2


# Typy zlozone

empty_list = []
other_list = [1, 2, 3, 4]
yet_another_list = [3, 'Bartek', [1, 4, 5]]
names = ['John', 'Terry', 'Eric']

len(names)
names.apend('Bartek')


def dec_to_bin_better(n):
    res = []
    while n > 0:
        res.append(n % 2)
        n = n // 2
    res.reverse()
    return res


meals = ['Spaghetti', 'Pizza', 'Haggis']

i = 0
while i < len(meals):
    print(f'{i}: {meals[i]}')
    i += 1

# petla 'for'

names = ['John', 'Terry', 'Eric']

for name in names:
    print(name)

prices_to_discount = [100, 30, 45, 76, 999]

for price in prices_to_discount:
    print(price * 0.8)

# napisy i sekwencje

' '.join(['It', 'will', 'be', 'separated', 'by', 'space'])

'Ten napis chce podzielic na spacjach'.split(' ')


def dec_to_bin_better(n):
    res = []
    while n > 0:
        res.apend(str(n % 2))
        n = n // 2
    res.reverse()
    return ''.join(res)

# funckja range


for i in range(4):
    print(i)

for i in range(2, 4):
    print(i)

for i in range(1, 4, 2):
    print(i)

res = []

for i in range(2, 101, 2):
    res.append(i * 7)

print(res)

# słowniki

user_data = {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Smith'
    }

print(user_data['id'])

id_str = 'id'                   # klucz jako string

user_data['id']                 # mozemy sie dobrac wprost przez klucz
user_data[id_str]               # mozemy sie tez dobrac przez wartosc klucza zadeklarowana w zmiennej
user_data['asd']                # wyzrzuca blad jak nie ma klucza w slowniku

user_data.get('id')             # mozemy tez uzyc metody 'get' dla slownika
user_data.get('asd')            # nie wyrzuci bledu gdy nie ma klucza w slowniku

n = user_data.get('asd')
type(n)                         # brak wartosci w sliwniku zwroci 'None'

a = user_data.get('asd', 'a')   # mozna zadeklarowac wartosc domyslna, ktora zostanie zwrocona zamiast 'None'


def name_as_list(data):
    string = data.get('name')
    return string.split(' ')


data = {'name': 'Józef Kowalski'}

my_list = name_as_list(data)    # wprzypdaku pustej listy wyrzuci blad
print(my_list)

data2 = {}

my_list2 = name_as_list(data2)


def name_as_list_better(data):
    string = data.get('name', '')   # deklarujemy co ma zwrocic gdy nie ma klucza, lub lista jest pusta
    return string.split(' ')


my_list2 = name_as_list_better(data2)    # tym razem bedzie ok
print(my_list2)


def calculate_price(base_price, data):
    percentage = data.get('price_percentage')
    if percentage is not None:
        new_price = base_price * percentage
    else:
        new_price = base_price
    return new_price


def calculate_price_better(base_price, data):
    percentage = data.get('price_percentage', 1)
    return base_price * percentage


invoice_data = {
    'id': 1,
    'name': 'Bill Gates',
    'address': {
        'city': 'Redmont',
        'country': 'US'
    },
    'price_percentage': 1.2
}

tshirt_price = 16
price_for_bill_gates = calculate_price(tshirt_price, invoice_data)
print(price_for_bill_gates)

invoice_data['price_percentage'] = 2.7  # mozemy modyfikowac wartosci dla klucza
invoice_data['price'] = 16              # jezeli nie ma klucza to zostanie utworzony nowy

invoice_data.pop('price')               # usuwa klucz-wartosc ze slownika

example_dict_in_dict = {'data': [       # slownik w slowniku
    {
        'id': 1,
        'name': 'John Smith'
    },
    {
        'id': 2,
        'name': 'Merry Sue'
    }
]}

# indeksowanie wewnatrz zagnieżdżonych słowników

example_dict_in_dict['data'][0]
example_dict_in_dict['data'][0]['name']


evens_mult_seven = {}

for i in range(0, 101, 2):
    evens_mult_seven[i] = i*7

print(evens_mult_seven)

# słownik i pętla for

for key in evens_mult_seven:
    print(key)

for key, value in evens_mult_seven.items():
    print(f'Liczba {key} * siedem to {value}')

'id' in user_data                               # sprawdzamy czy klucz znajduje się w słowniku

# Zbiory

part_of_alphabet = {'a', 'b', 'c'}
part_of_alphabet.add('a')

volves = {'a', 'e', 'y', 'u', 'i', 'o'}

my_name = 'bartek'

for i in my_name:
    if i in volves:
        print(i)

# Krotki (tuple)

some_tuple = (1, 'John', 'Smith')
some_tuple[0]

id, name, surname = some_tuple  # krotki możemy rozpakowywać

print(id)
print(name)

point = (4, 5)
x, y = point
print(x)
print(y)

# Sekwencje cd...

# funkcja zip

# zwraca krotke z kolejnymi wartosciami z podanych jej sekwencji

ex_names = ['Zad. 1', 'Zad. 2', 'Zad. 3']
marks = [5.5, 3, 4]

for name, mark in zip(ex_names, marks):
    print(f'{name}: {mark}')

marks_dicts = dict(zip(ex_names, marks))

# list comprehensions

my_list = []
for n in range(7):
    if n % 3 == 0:
        my_list.append(n)
print(my_list)

my_list_with_comp = [n for n in range(7) if n % 3 == 0]             # alternatywna dla petli - wyrazenie listowe
print(my_list_with_comp)


# sortowanie bąbelkowe - piszemy algorytm

unsorted_list = [7, 4, 8, 1]


def bubble_sort(data):
    #n = len(data) - 1
    for n in range(len(data) - 1, 0, -1):
        for j in range(n):
            print(f'Lista: {data}; obieg ({n}, {j})')
            if data[j] > data[j+1]:
                print(f'Zamieniam {data[j]} z {data[j+1]}')
                data[j], data[j+1] = data[j+1], data[j]             # swap zamiana kolejnosci elemtntów listy



bubble_sort(unsorted_list)

print(unsorted_list)

# funkcje cd..

# args i kwargs


def arbitrary_args(*args, **kwargs):
    print(args)                                                     # zwraca argumenty pozycyjne
    print(kwargs)                                                   # zwraca argumenty z kluczem


arbitrary_args(5, 'Abra', 'Kadabra', name='John', surname='Cleese')


def send_request(url, method='POST', **kwargs):
    print(url)
    print(method)
    print(kwargs)


send_request('https://httpbin.org/', token='JWT erf XXX', accept_encoding='UTF-8')
send_request('https://httpbin.org/', method='GET', token='JWT erf XXX', accept_encoding='UTF-8')


# dokumentacja funkcji

def buy_fb_likes(country, how_many):
    """Allows to buy likes on facebook"""
    print(f'Congrats! You\'ve bought {how_many} '
          f'Faceook likes form {country}')




