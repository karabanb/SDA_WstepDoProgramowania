
if __name__ == '__main__':

    # Zadanie 1. 1. 1 obrazek

    print('  _______  \n@/  . .  \\@\n\n(  \\___/  )\n\n \\_______/')

    # Zadanie 1. 1. 2

    a = 55
    b = 10

    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
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
    seconds = int(hours)*3600
    print(f'Jest to: {seconds}')

# zadanie 1. 1. 6

    celsius = input('Podaj liczbę stopni celsjusza:')
    kelwin = int(celsius)+273.15
    fahrenheit = 32 + (9/5 * int(celsius))

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

    bmi = weight/(height/100)**2

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

    celsius = input('Podaj liczbę stopni celsjusza:')
    k_or_f = []

    while k_or_f not in ['k', 'f']:
        k_or_f = str(input('Przeliczyć na Kelwiny czy Fahrenheity? (k/f):'))
        if k_or_f == 'k':
            kelwin = int(celsius) + 273.15
            print(f'{celsius} stopni C to : {kelwin} K')
        else:
            fahrenheit = 32 + (9 / 5 * int(celsius))
            print(f'{celsius} stopni C to : {fahrenheit} F')