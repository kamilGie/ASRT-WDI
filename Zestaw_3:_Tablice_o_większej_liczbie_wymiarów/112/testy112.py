import unittest
import os
import sys
import importlib

from szablon112 import Zadanie_112


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

    def test_Nr01_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1)

    def test_Nr02_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 1)

    def test_Nr03_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]), 2)

    def test_Nr04_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0]]), 2)

    def test_Nr05_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]), 2)

    def test_Nr06_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 0, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]), 2)

    def test_Nr07_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]), 3)

    def test_Nr08_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0]]), 3)

    def test_Nr09_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0]]), 2)

    def test_Nr10_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0]]), 2)

    def test_Nr11_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0]]), 3)

    def test_Nr12_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0]]), 3)

    def test_Nr13_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1], [0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0], [1, 1, 0, 0, 1, 0]]), 3)

    def test_Nr14_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0]]), 3)

    def test_Nr15_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1, 0]]), 4)

    def test_Nr16_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]), False)

    def test_Nr17_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 0], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]), False)

    def test_Nr18_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]), 2)

    def test_Nr19_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]), False)

    def test_Nr20_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[1, 0, 1, 1, 0], [0, 1, 0, 0, 1], [1, 0, 1, 1, 0], [0, 1, 0, 0, 1], [1, 0, 1, 1, 0]]), 3)

    def test_Nr21_Zadanie_112_argumenty_tablica(self):
            self.assertEqual(Zadanie_112([[0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]), 2)


