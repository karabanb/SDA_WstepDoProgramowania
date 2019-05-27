
import itertools as iter

if __name__ == '__main__':

    # Zadanie 1. 1. 1 obrazek

    print('  _______  \n@/  . .  \\@\n\n(  \\___/  )\n\n \\_______/')

    # Zadanie 1. 1. 2

    a = 55
    b = 10

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)

    # zadanie 1. 1. 3

    print(f'a + b = {a + b}')
    print(f'a - b = {a - b}')
    print(f'a * b = {a * b}')
    print(f'a / b = {a / b}')
    print(f'a % b = {a % b}')

    # zadanie 1. 1. 4

    radius = input('Podaj promień:')
    obwod = int(radius) * 2 * 3.14
    print(f'Obwód to: {obwod}')

    # zadanie 1. 1. 5

    hours = input('Podaj liczbę godzin:')
    seconds = int(hours) * 3600
    print(f'Jest to: {seconds}')

    # zadanie 1. 1. 6

    celsius = input('Podaj liczbę stopni celsjusza:')
    kelwin = int(celsius) + 273.15
    fahrenheit = 32 + (9 / 5 * int(celsius))

    print(f'{celsius} stopni C to : {kelwin} K\n'
          f'{celsius} stopni C to : {fahrenheit} F')

    # zadanie 1. 1. 7

    celsius = input('Podaj liczbę stopni celsjusza:')
    k_or_f = input('Przeliczyć na Kelwiny czy Fahrenheity? (k/f):')

    if k_or_f == 'k':
        kelwin = int(celsius) + 273.15
        print(f'{celsius} stopni C to : {kelwin} K')
    elif k_or_f == 'f':
        fahrenheit = 32 + (9 / 5 * int(celsius))
        print(f'{celsius} stopni C to : {fahrenheit} F')
    else:
        print('Coś wpisałeś nie tak:/')

    # zadanie 1. 1. 8

    speed = int(input('Podaj prędkość w km/h:'))
    if speed > 50:
        print('Z taką prędkością to na autostradę')
    elif speed > 0:
        print('taką prędkością możesz poruszać się po mieście')
    else:
        print('Coś wpisałeś nie tak:/')

    # zadanie 1. 1. 9

    weight = int(input('Podaj swoją wagę (kg):'))
    height = int(input('Podaj swój wzrost (cm):'))

    bmi = weight / (height / 100) ** 2

    if bmi >= 25:
        print('nadwaga')
    elif bmi > 18.5:
        print('ok')
    else:
        print('niedowaga')

    # zadaie 2. 1. 1

    c = 0

    while c <= 100:
        print(c)
        c += 7

    # zadanie 2. 1. 2

    number = int(input('Podaj dowolną liczbę:'))

    while number <= 1000:
        number = number * 2
        print(number)

    # zdanie 2. 1. 3

    star = '*'
    while len(star) < 5:
        print(star)
        star = star + '*'

    for i in range(5):
        print('*' * i)

    # zadanie 2. 1. 4

    while True:
        user_answer = str(input('Czy chcesz zakończyć pracę?:'))
        if user_answer == 'y':
            break

    # zadanie 2. 1. 5

    celsius = input("Podaj liczbę stopni celsjusza:")
    k_or_f = str(input('Przeliczyć na Kelwiny czy Fahrenheity? (k/f):'))

    if k_or_f == 'k':
        kelwin = int(celsius) + 273.15
        print(f'{celsius} stopni C to : {kelwin} K')
    if k_or_f == 'f':
        fahrenheit = 32 + (9 / 5 * int(celsius))
        print(f'{celsius} stopni C to : {fahrenheit} F')

    else:
        while k_or_f not in ['k', 'f']:
            k_or_f = str(input('Przeliczyć na Kelwiny czy Fahrenheity? (k/f):'))
            if k_or_f == 'k':
                kelwin = int(celsius) + 273.15
                print(f'{celsius} stopni C to : {kelwin} K')
                break
            if k_or_f == 'f':
                fahrenheit = 32 + (9 / 5 * int(celsius))
                print(f'{celsius} stopni C to : {fahrenheit} F')
                break

    # Zadanie 2. 1. 6

    word = str(input('Podaj napis:'))
    number = int(input('Podaj liczbę:'))

    for i in range(number):
        print(word)

    # Zadanie 2. 2. 1.

    import numpy as np
    some_numbers = list(np.random.random_sample(10))

    i = 0
    max_num = some_numbers[i]

    while i < len(some_numbers):
        if some_numbers[i] > max_num:
            max_num = some_numbers[i]
        i += 1

    max_num == max(some_numbers)

    # zadanie 2. 2. 2

    some_numbers = list(np.random.randint(10, 100, 10))

    i = 0
    max_num = some_numbers[i]

    while i < len(some_numbers):
        if some_numbers[i] > max_num:
            max_num = some_numbers[i]
        i += 1

    print(f' najwieksza liczba to: {max_num}, jej indeks to: {i}')

    # rozwiazaie Olka

    i = 0
    max_value = some_numbers[i]

    for item in some_numbers:
        if max_value < item:
            max_value = item

    # zadanie 2. 2. 3

    some_numbers = list(np.random.randint(10, 100, 10))

    for i in some_numbers:
        if i % 3 == 0:
            print(f' Liczba {i} jest podzielna przez 3')

    # zadanie 2. 2. 4

    for i in range(15):
        print(i**2)

    # zadanie 2. 3. 1

    name = input('Podaj swoje imię: ')
    length = 0

    for i in name:
        length += 1

    print(f'Twoje imię ma {length} liter(y)')

    name = input('Podaj swoje imię: ')
    length = len(name)
    print(f'Twoje imię ma {length} liter(y)')

    # zadanie 2. 3. 2

    name = str(input('Podaj swoje imię: '))

    if name.endswith('a'):
        print('Istnieje niezerowe prawdopodobiństwo, że to imię żeńskie.')

    # zadanie 2. 3. 3

    male_names_with_a = {'Kosma'}
    female_names_without_a = {'Miriam'}

    name = str(input('Podaj swoje imię: '))

    if name in male_names_with_a:
        print('Jest to imię męskie')
    elif name in female_names_without_a:
        print('Jest to imię żeńskie')
    elif name.endswith('a'):
        print('Jest to imię żeńskie')
    else:
        print('Jest to imię męskie')

    # zadanie 2. 3. 4

    # zadanie 2. 3. 5

    # zadanie 2. 3. 6

    # zadanie 2. 3. 7

    # zadanie 3. 1. 1

    def area(r):
        circuit = 3.14 * r ** 2
        return circuit

    # zadanie 3. 1. 2

    def smaller_int(x, y):
        result = [x, y]
        return min(result)

    # zadanie 3. 1. 3

    def greater_int(x, y):
        result = [x, y]
        return max(result)

    # zadanie 3. 1. 4

    def division(x, y):
        if x % y == 0:
            return True
        else:
            return False

    # zadanie 3. 1. 5

    def str_multiple(string, n):
        for j in range(n):
            print(string)

    # zadanie 3. 1. 6

    def leap_year(rok):
        years = []
        year = rok
        while len(years) < 10:
            if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                years.append(year)
            year += 1
        return years

    # zadanie 3. 1. 7

    def palindorme(words):
        return words == words[::-1]

    # zadanie 3. 1. 8

    def name_concat(name, surname):
        return ' '.join([name, surname])


    # zadanie 3. 2. 1

    some_list = ['Bartek', 'Aleksander', 3, 'Damian']


    def max_len(some_list):
        max_len = some_list[0]
        for i in some_list:
            if len(str(max_len)) < len(str(i)):
                max_len = str(i)
        return max_len

    # zadanie 3. 2. 2

    def reverse_list(x):
        x.reverse()
        return x

    # zadanie 3. 2. 3

    def check_existing(element, elements):
        return element in elements

    # zadanie 3. 2. 4

    def even_elements(input):
        even_indexes = []
        for i in range(len(input)):
            if i % 2 == 0:
                even_indexes.append(input[i])
        return even_indexes

    # zadanie 3. 2. 5

    def sum_list(input):
        return sum(input)

    # alternatywnie

    def sum_list(input):
        added = 0
        for i in range(len(input)):
            added += input[i]
        return added

    # zadanie 3. 2. 6

    def the_longest_word(input):
        max_word = input[0]
        for word in input:
            if len(word) > len(max_word):
                max_word = word
        return max_word

    # zadanie 3. 2. 7

    def append_no_duplication(my_list, new_element):
        if new_element not in my_list:
            my_list.append(new_element)
        return my_list

    # zadanie 3. 2. 8

    def print_frames(list_to_print):
        for word in list_to_print:
            print('*' * len(word) + '****')
            print(f'* {word} *')
            print('*' * len(word) + '****')


    # zadanie 3. 3. 1

    my_first_dict = {
        'id': 1,
        'first_name': 'Bartek',
        'last_name': 'Karaban'
    }


    def exist_in_dict(element, my_dict):
        return element in my_dict

    # zadanie 3. 3. 2

    def key_value(my_dict):
        for key, value in my_dict.items():
            print(f' key: {key}, value: {value}')

    # zadanie 3. 3. 3

    def squared_keys(n):
        output = {}
        for i in range(n):
            output[i] = i**2
        return output

    # zadanie 3. 3. 4

    def sum_of_dict(my_dict):
        return sum(my_dict.values())

    # zadanie 3. 3. 5

    def remove_key(my_dict, my_key):
        my_dict.pop(my_key)

    # zadanie 3. 3. 6

    def remove_keys(my_dict, keys):
        for key in keys:
            my_dict.pop(key)

    # zadanie 3. 3. 7

    def max_in_dict(my_dict):
        return max(my_dict.values())

    # zadanie 3. 3. 8

    letters = {1: ['a', 's'], 2: ['b', 'c']}

    def dict_comb(my_dict):
        pass
        combs = []
        vals = []
        for key, value in my_dict.items():
            print(key)
            print(value)

    # zadanie 3. 3. 9

    sentence = 'Napisz zdanie. Jakieś zwykłe zdanie.'

    def count_words(some_sentence):
        words_count = []
        words = sentence.split(' ')
        for word in words:
            words_count.append(words.count(word))
        return dict(zip(words, words_count))

    print(count_words(sentence))

    # zadanie 3. 3. 10

    def count_letters(some_word):
        letters_count = []
        letters = list(some_word)
        for letter in letters:
            letters_count.append(letters.count(letter))
        return dict(zip(letters, letters_count))

    print(count_letters('bannana'))

    # better???

    def count_letter_more_pythonic(some_word):
        letters = list(some_word)
        letters_count = []
        return dict(zip(letters, [letters_count.append(letters.count(letter)) for letter in letters]))

    print(count_letters('bannana'))

    # zadanie 3. 3. 11

    users = {'bkaraban': 'chujidupa',
             'jankowalski': 'janek69',
             'admin': 'admin1'}

    def authorize(users, username, password):
        if users[username] == password:
            return True
        else:
            return False

















