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


