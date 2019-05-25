

import os
import pathlib

if __name__ == '__main__':

    print(dir())
    print(__file__)
    print(os.path.realpath(__file__))
    base_dir = os.path.dirname(os.path.realpath(__file__)) # ścieżka do obecnego katalogu
    print(base_dir)

    file_near_me = os.path.join(base_dir, 'first_program.py')
    print(file_near_me)

    file_near_me_sub = os.path.join(os.path.join(base_dir, "subdir"), "some_file")
    print(file_near_me_sub)

    # katalog wyżej

    dir_up = os.path.dirname(base_dir)
    print(dir_up)

    # czy plik istnieje?

    print(os.path.isfile(file_near_me_sub))
    print(os.path.isfile(file_near_me))

    # alternatywnie w pathlib

    path = pathlib.Path(__file__).resolve().parent.parent.joinpath('file.py')
    print(path)