import unittest
from contextlib import redirect_stdout
import io

from szablon20 import Zadanie_20


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

    def test_Nr01_Zadanie_20(self):
            self.assertEqual(Zadanie_20(10), 24)

    def test_Nr02_Zadanie_20(self):
            self.assertEqual(Zadanie_20(24), 49)

    def test_Nr03_Zadanie_20(self):
            self.assertEqual(Zadanie_20(2), 4)

    def test_Nr04_Zadanie_20(self):
            self.assertEqual(Zadanie_20(5), 5)

    def test_Nr05_Zadanie_20(self):
            self.assertEqual(Zadanie_20(10), 24)

    def test_Nr06_Zadanie_20(self):
            self.assertEqual(Zadanie_20(120), 386)

    def test_Nr07_Zadanie_20(self):
            self.assertEqual(Zadanie_20(215), 8758)

    def test_Nr08_Zadanie_20(self):
            self.assertEqual(Zadanie_20(47), 246)


