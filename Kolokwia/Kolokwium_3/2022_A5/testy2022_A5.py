import unittest
from contextlib import redirect_stdout
import io

from szablon2022_A5 import magic


class testy(unittest.TestCase):

    def test_Nr01_magic(self):
        self.assertEqual(
            magic([[3, 11, 14, 17], [6, 12, 7, 9], [10, 8, 16, 13], [5, 15, 4, 2]]),
            True,
        )

    def test_Nr02_magic(self):
        self.assertEqual(
            magic([[17, 15, 16, 14], [6, 3, 4, 9], [10, 12, 11, 13], [5, 8, 7, 2]]),
            True,
        )

    def test_Nr03_magic(self):
        self.assertEqual(
            magic([[17, 8, 4, 14], [6, 15, 11, 9], [10, 3, 7, 13], [5, 12, 16, 2]]),
            True,
        )

    def test_Nr04_magic(self):
        self.assertEqual(magic([[4, 9, 2], [3, 5, 7], [8, 1, 6]]), False)

    def test_Nr05_magic(self):
        self.assertEqual(magic([[4, 9, 2], [3, 5, 7], [8, 1, 6]]), False)

    def test_Nr06_magic(self):
        self.assertEqual(magic([[5, 5, 5], [5, 5, 5], [5, 5, 5]]), True)

    def test_Nr07_magic(self):
        self.assertEqual(magic([[10, 20, 30], [20, 30, 10], [30, 10, 20]]), False)

    def test_Nr08_magic(self):
        self.assertEqual(magic([[4, 14, 18], [7, 5, 9], [13, 1, 11]]), False)

    def test_Nr09_magic(self):
        self.assertEqual(
            magic([[17, 3, 4, 14], [11, 9, 6, 12], [10, 8, 7, 13], [5, 15, 16, 2]]),
            True,
        )

    def test_Nr10_magic(self):
        self.assertEqual(
            magic([[17, 3, 4, 14], [9, 6, 12, 11], [13, 10, 8, 7], [5, 15, 16, 2]]),
            True,
        )

    def test_Nr11_magic(self):
        self.assertEqual(
            magic([[16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 6, 12], [4, 14, 15, 1]]),
            False,
        )


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "Istnieją 4 możliwe kombinacje dwóch operacji: dwa przesunięcia w wierszach, dwa przesunięcia w kolumnach, lub jedno przesunięcie w wierszu i jedno w kolumnie.",
        "Przekształcaj oryginalną tablicę w każdej z 4 kombinacji i dla każdej kolumny i wiersza sprawdzaj, czy suma elementów w każdym wierszu i każdej kolumnie jest równa.",
        "Zapisz oryginalną tablicę, stwórz jej kopię, a następnie obracaj kopię. Podczas rotacji zapamiętaj ostatni element wiersza/kolumny, przesuwaj każdy element w kierunku rotacji, a na koniec wstaw ostatni element na początek.",
    ]
    print(podpowiedzi[nr - 1])


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
