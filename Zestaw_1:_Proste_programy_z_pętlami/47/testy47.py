import unittest

from szablon47 import Zadanie_47


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_47(self):
        self.assertEqual(Zadanie_47(1370), 1234)

    def test_Nr02_Zadanie_47(self):
        self.assertEqual(Zadanie_47(1521), 1370)

    def test_Nr03_Zadanie_47(self):
        self.assertEqual(Zadanie_47(1000), 901)

    def test_Nr04_Zadanie_47(self):
        self.assertEqual(Zadanie_47(2115), 1905)

    def test_Nr05_Zadanie_47(self):
        self.assertEqual(Zadanie_47(2312), 2082)

    def test_Nr06_Zadanie_47(self):
        self.assertEqual(Zadanie_47(3251), 2928)

    def test_Nr07_Zadanie_47(self):
        self.assertEqual(Zadanie_47(2357), 2122)

    def test_Nr08_Zadanie_47(self):
        self.assertEqual(Zadanie_47(1231), 1109)

    def test_Nr09_Zadanie_47(self):
        self.assertEqual(Zadanie_47(100), 91)

    def test_Nr10_Zadanie_47(self):
        self.assertEqual(Zadanie_47(10), -1)

    def test_Nr11_Zadanie_47(self):
        self.assertEqual(Zadanie_47(11), 10)

    def test_Nr12_Zadanie_47(self):
        self.assertEqual(Zadanie_47(345), 311)

    def test_Nr13_Zadanie_47(self):
        self.assertEqual(Zadanie_47(23), 21)


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
