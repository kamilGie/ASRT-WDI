import unittest
from contextlib import redirect_stdout
import io

from szablon194 import Zadanie_194
from szablon194 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([15, 19] ,Node( [2, 5] ,Node( [7, 11] ,Node( [8, 12] ,Node( [5, 6] ,Node( [13, 17])))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[13, 19] -> [2, 6] -> [7, 12]', msg=f"dla zmiennych: Node([15, 19] ,Node( [2, 5] ,Node( [7, 11] ,Node( [8, 12] ,Node( [5, 6] ,Node( [13, 17])))))). Otrzymano: {wynik}, oczekiwano: '[13, 19] -> [2, 6] -> [7, 12]'")

    def test_Nr02_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([1, 4] ,Node( [2, 3] ,Node( [5, 8] ,Node( [6, 7])))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[1, 4] -> [5, 8]', msg=f"dla zmiennych: Node([1, 4] ,Node( [2, 3] ,Node( [5, 8] ,Node( [6, 7])))). Otrzymano: {wynik}, oczekiwano: '[1, 4] -> [5, 8]'")

    def test_Nr03_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([10, 20] ,Node( [15, 25] ,Node( [30, 40] ,Node( [35, 45])))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[10, 25] -> [30, 45]', msg=f"dla zmiennych: Node([10, 20] ,Node( [15, 25] ,Node( [30, 40] ,Node( [35, 45])))). Otrzymano: {wynik}, oczekiwano: '[10, 25] -> [30, 45]'")

    def test_Nr04_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([1, 2] ,Node( [3, 4] ,Node( [5, 6] ,Node( [7, 8])))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[1, 2] -> [3, 4] -> [5, 6] -> [7, 8]', msg=f"dla zmiennych: Node([1, 2] ,Node( [3, 4] ,Node( [5, 6] ,Node( [7, 8])))). Otrzymano: {wynik}, oczekiwano: '[1, 2] -> [3, 4] -> [5, 6] -> [7, 8]'")

    def test_Nr05_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([0, 3] ,Node( [1, 5] ,Node( [4, 6] ,Node( [7, 10])))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[0, 6] -> [4, 6] -> [7, 10]', msg=f"dla zmiennych: Node([0, 3] ,Node( [1, 5] ,Node( [4, 6] ,Node( [7, 10])))). Otrzymano: {wynik}, oczekiwano: '[0, 6] -> [4, 6] -> [7, 10]'")

    def test_Nr06_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([10, 15] ,Node( [12, 18] ,Node( [20, 25] ,Node( [23, 28])))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[10, 18] -> [20, 28]', msg=f"dla zmiennych: Node([10, 15] ,Node( [12, 18] ,Node( [20, 25] ,Node( [23, 28])))). Otrzymano: {wynik}, oczekiwano: '[10, 18] -> [20, 28]'")

    def test_Nr07_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([1, 3] ,Node( [2, 4] ,Node( [5, 7] ,Node( [6, 8])))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[1, 4] -> [5, 8]', msg=f"dla zmiennych: Node([1, 3] ,Node( [2, 4] ,Node( [5, 7] ,Node( [6, 8])))). Otrzymano: {wynik}, oczekiwano: '[1, 4] -> [5, 8]'")

    def test_Nr08_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([5, 10] ,Node( [15, 20] ,Node( [25, 30]))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[5, 10] -> [15, 20] -> [25, 30]', msg=f"dla zmiennych: Node([5, 10] ,Node( [15, 20] ,Node( [25, 30]))). Otrzymano: {wynik}, oczekiwano: '[5, 10] -> [15, 20] -> [25, 30]'")

    def test_Nr09_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([3, 5] ,Node( [4, 6] ,Node( [5, 7] ,Node( [8, 10])))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[3, 7] -> [5, 7] -> [8, 10]', msg=f"dla zmiennych: Node([3, 5] ,Node( [4, 6] ,Node( [5, 7] ,Node( [8, 10])))). Otrzymano: {wynik}, oczekiwano: '[3, 7] -> [5, 7] -> [8, 10]'")

    def test_Nr10_Zadanie_194(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_194(Node([1, 10] ,Node( [2, 9] ,Node( [3, 8] ,Node( [4, 7])))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[1, 10] -> [3, 8]', msg=f"dla zmiennych: Node([1, 10] ,Node( [2, 9] ,Node( [3, 8] ,Node( [4, 7])))). Otrzymano: {wynik}, oczekiwano: '[1, 10] -> [3, 8]'")


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

