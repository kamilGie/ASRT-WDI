import unittest
from contextlib import redirect_stdout
import io

from szablon2022_B6 import separate
from szablon2022_B6 import Node


class testy(unittest.TestCase):

    def test_Nr01_separate(self):
        f = io.StringIO()
        with redirect_stdout(f):
            _, _, deleted_cnt = separate( ( lambda n: ( setattr( n, "next", Node(2, Node(3, Node(-1, Node(-2, Node(-3, n)))))), n,)[1])(Node(1)))

        self.assertEqual(deleted_cnt, 3)


    def test_Nr05_separate(self):
        f = io.StringIO()
        with redirect_stdout(f):
            _,_,deleted_cnt = separate( (lambda n: (setattr(n, "next", Node(2, n)), n)[1])(Node(1)))
        self.assertEqual(deleted_cnt, 1)
        

    def test_Nr06_separate(self):
        f = io.StringIO()
        with redirect_stdout(f):
            _,_,deleted_cnt = separate( ( lambda n: ( setattr(n, "next", Node(4, Node(6, Node(-1, Node(-3, n))))), n,)[1])(Node(2)))

        self.assertEqual(deleted_cnt,0)


def podpowiedz(nr: int):
    podpowiedzi = [
        "Odłączenie węzła w liście cyklicznej przerywa jej cykliczność.",
        "Stwórz dwie nowe listy z wartownikiem (głową i ogonem), a na koniec ustaw ogon tak, aby wskazywał na głowę, tworząc cykl.",
        "Odłączaj węzły po kolei: jeśli klucz jest dodatni i parzysty, dodaj go do ogona listy dodatnich parzystych; jeśli klucz jest ujemny i nieparzysty, dodaj go do ogona listy ujemnych nieparzystych. Jeśli klucz nie pasuje do żadnej listy, wystarczy go odłączyć i zwiększyć licznik usuniętych węzłów."
    ]
    print(podpowiedzi[nr - 1])


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def komenda(k: str, *args, **kwargs):
    """
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu


    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    """
    import os
    import sys
    import importlib

    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )
