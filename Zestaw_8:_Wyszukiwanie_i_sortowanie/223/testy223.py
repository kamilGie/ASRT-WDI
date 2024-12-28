import unittest
from contextlib import redirect_stdout
import io

from szablon223 import Zadanie_223


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

    def test_Nr01_Zadanie_223(self):
            self.assertEqual(Zadanie_223([1,1,1,1,1,2,2,2,4,5],2), 3)

    def test_Nr02_Zadanie_223(self):
            self.assertEqual(Zadanie_223([1,1,1,1,1,1,2,3,3,3,4,5],4), 1)

    def test_Nr03_Zadanie_223(self):
            self.assertEqual(Zadanie_223([1,1,1,1,1],1), 5)

    def test_Nr04_Zadanie_223(self):
            self.assertEqual(Zadanie_223([1,2,3,4,5],6), 0)

    def test_Nr05_Zadanie_223(self):
            self.assertEqual(Zadanie_223([7],7), 1)

    def test_Nr06_Zadanie_223(self):
            self.assertEqual(Zadanie_223([1] * 1_000_000,1), 1000000)

    def test_Nr07_Zadanie_223(self):
            self.assertEqual(Zadanie_223([i for i in range(1, 1001) for _ in range(1000)],69), 1000)

    def test_Nr08_Zadanie_223(self):
            self.assertEqual(Zadanie_223([2] * 500_000 + [3] * 500_000,2), 500000)

    def test_Nr09_Zadanie_223(self):
            self.assertEqual(Zadanie_223([1] + [2] * 999_998 + [3],1), 1)

    def test_Nr10_Zadanie_223(self):
            self.assertEqual(Zadanie_223([1] + [2] * 999_998 + [3],2), 999998)

    def test_Nr11_Zadanie_223(self):
            self.assertEqual(Zadanie_223([1] + [2] * 999_998 + [3],3), 1)

    def test_Nr12_Zadanie_223(self):
            self.assertEqual(Zadanie_223([1] + [2] * 999_998 + [3],4), 0)


