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

    def palindorme(word):
        return word == word[::-1]

    # zadanie 3. 1. 8

    def name_concat(name, surname):
        return ' '.join([name, surname])



