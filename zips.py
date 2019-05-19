
labels = ['Lobo', 'Ligo', 'Macintosh', 'Champion', 'Antonówka']
prices_190519 = [90, 200, 120, 220, 300]
prices_260519 = [90, 220, 90, 250, 200]

print(zip(labels, prices_190519, prices_260519))                      # nic nie pokaze bo zip to generator

print(list(zip(labels, prices_190519, prices_260519)))                # teraz juz tak, bo zrucilismy efekt zipa do listy

my_list_implementation = []                                           # implementacja powyzszego tylko w petli
for label, price in zip(labels, prices_190519):
    tuple_again = (label, price)
    my_list_implementation.append((label, price))
print(my_list_implementation)

my_list_implementation2 = []                                          # implementacja ale ze spakowana krotka
for my_tuple in zip(labels, prices_260519):
    my_list_implementation2.append(my_tuple)
print(my_list_implementation2)

for label, price in zip(labels, prices_190519):                       # przykład kiedy nie chcemy pakować krotek
    print(f'Jabłka {label} kosztowały {price}')


my_first_dict_with_prices = {}
for label, price in zip(labels, prices_190519):
    my_first_dict_with_prices[label] = price

dict_with_prices = dict(zip(labels, prices_190519))                   # budowa slownika z dwoch list



