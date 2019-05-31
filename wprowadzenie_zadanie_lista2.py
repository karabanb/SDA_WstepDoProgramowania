
if __name__ == '__main__':

    # 1. Sekwencje
    # 1. 1. 1.

    first_names = ['John', 'Terry', 'Eric']
    last_names = ['Cleese', 'Gilliam', 'Idle']

    def welcome(first_names, last_names):
        for key, value in zip(first_names, last_names):
            print(f' Hello!, {key}  {value}!')

    # 1. 1. 2

    labels = ['name', 'address', 'message']
    data = [['Robert Musiała', 'plac Łanowa 634\n39-176 Tczew',
             'Popularny ręka prosty stacja sobota. Jedynie przypadek stopaprawny.\n'
             'Tworzyć pijany umieścić kto płot uderzyć rzecz głowa. Wyspa mistrzwyjście pytanie kij.'],
            ['Natan Świerszcz', 'aleja Solidarnosci 70\n78-022 Piła',
             'Dzielić położenie znajdować się znosić. Smutny rezultat żydowski Janwojna ofiara zwycięstwo. Temperatura fakt ludzki wchodzić chyba wspólnota.\n'
             'Sólcodzienny przyczyna plemię. Skóra brzydki palić.'],
            ['Justyna Towarek', 'pl. Szkolna 56/45\n83-060 Jaworzno',
             'Wracać akcja sześćdziesiąt postępowanie człowiek Belgia oznaczać.Śmierć pamiętać wartość kultura uprawiać gotowy umrzeć. Artystyczny numerusługa sierpień one dwa wewnętrzny.'],
            ['Gaja Harasimiuk', 'ul. Pomorska 267\n24-027 Siedlce', 'Stół kwiecień młody jej.'],
            ['Marcin Welc', 'ulica Toruńska 92\n23-261 Wyszków',
             'Wizyta babcia operacja czoło życie ciepło telewizyjny. Wraz silnikświęty kwiat dyskusja.']]

    new_list = []

    for chunk in data:
        new_list.append(dict(zip(labels, chunk)))


    # zadanie 1. 2. 1

    dna = ['A', 'G', 'G', 'T', 'C']

    def replicate_dna(dna):
        replicated_dna = []
        letters = {'A': 'T',
                   'T': 'A',
                   'G': 'C',
                   'C': 'G'}

        for i in range(len(dna)):
            letter = dna[i]
            replicated_dna.append(letters[letter])
        return replicated_dna

    # zadanie 1. 3. 1.

    def get_abolute_zero(scale='K'):
        zeros = {
            'K': 0,
            'C': -273.15,
            'F': -459.67
        }
        print(zeros[scale])

    # zadanie 1. 4. 1.









