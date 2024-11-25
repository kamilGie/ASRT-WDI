import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon132 import Zadanie_132


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
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_132_argumenty_4_3(self):
            self.assertEqual(Zadanie_132(4, 3), 4)

    def test_Nr02_Zadanie_132_argumenty_5_0(self):
            self.assertEqual(Zadanie_132(5, 0), 1)

    def test_Nr03_Zadanie_132_argumenty_7_2(self):
            self.assertEqual(Zadanie_132(7, 2), 21)

    def test_Nr04_Zadanie_132_argumenty_6_3(self):
            self.assertEqual(Zadanie_132(6, 3), 20)

    def test_Nr05_Zadanie_132_argumenty_20_19(self):
            self.assertEqual(Zadanie_132(20, 19), 20)

    def test_Nr06_Zadanie_132_argumenty_5_3(self):
            self.assertEqual(Zadanie_132(5, 3), 10)

    def test_Nr07_Zadanie_132_argumenty_12_8(self):
            self.assertEqual(Zadanie_132(12, 8), 495)

    def test_Nr08_Zadanie_132_argumenty_12_11(self):
            self.assertEqual(Zadanie_132(12, 11), 12)

    def test_Nr09_Zadanie_132_argumenty_5_5(self):
            self.assertEqual(Zadanie_132(5, 5), 1)

    def test_Nr10_Zadanie_132_argumenty_11_2(self):
            self.assertEqual(Zadanie_132(11, 2), 55)

    def test_Nr11_Zadanie_132_argumenty_13_10(self):
            self.assertEqual(Zadanie_132(13, 10), 286)


