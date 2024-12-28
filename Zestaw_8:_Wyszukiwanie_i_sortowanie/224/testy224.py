import unittest
from contextlib import redirect_stdout
import io

from szablon224 import Zadanie_224


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


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
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_224(self):
            self.assertEqual(Zadanie_224([i for i in range(1, 1_000_001)],999_999), 999998)

    def test_Nr02_Zadanie_224(self):
            self.assertEqual(Zadanie_224([i for i in range(1, 1_000_001)],2115), 2114)

    def test_Nr03_Zadanie_224(self):
            self.assertEqual(Zadanie_224([i for i in range(1, 1_000_001)],1410), 1409)

    def test_Nr04_Zadanie_224(self):
            self.assertEqual(Zadanie_224([i for i in range(1, 1_000_001)],0), -1)

    def test_Nr05_Zadanie_224(self):
            self.assertEqual(Zadanie_224([i for i in range(1, 1_000_001)],123123123123), -1)

    def test_Nr06_Zadanie_224(self):
            self.assertEqual(Zadanie_224([i for i in range(1, 10_000_001)],1), 0)

    def test_Nr07_Zadanie_224(self):
            self.assertEqual(Zadanie_224([i for i in range(1, 10_000_001)],2115), 2114)

    def test_Nr08_Zadanie_224(self):
            self.assertEqual(Zadanie_224([i for i in range(1, 10_000_001)],21525124), -1)

    def test_Nr09_Zadanie_224(self):
            self.assertEqual(Zadanie_224([i for i in range(1, 10_000_001)],10_000_000), 9999999)


