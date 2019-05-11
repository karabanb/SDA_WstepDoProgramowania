
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
print(f'Hello, {name}')             # konstrukcja fstring
print(name)

# sprawdzanie typu zmiennej

x = 14
x = 'qwerty'

type(x)

# sprawdzenie obiektu w pamięci - zmienne to etykiety

a = 42
b = 42

id(a)
id(b)                               # sa to te same obikety ale o innej etykiecie

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




