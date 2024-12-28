import unittest
from contextlib import redirect_stdout
import io

from szablon228 import selection_sort, remove_max
from szablon228 import Node

class testy(unittest.TestCase):

    def test_Nr01_selection_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = selection_sort(Node(3, Node(2, Node(1))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3', msg=f"dla zmiennych: Node(3, Node(2, Node(1))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3'")

    def test_Nr02_selection_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = selection_sort(Node(5, Node(4, Node(3, Node(2, Node(1))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5', msg=f"dla zmiennych: Node(5, Node(4, Node(3, Node(2, Node(1))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5'")

    def test_Nr03_selection_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = selection_sort(Node(1, Node(3, Node(2, Node(123, Node(100, Node(23, Node(123, Node(923, Node(4213, Node(312, Node(2115))))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 23 -> 100 -> 123 -> 123 -> 312 -> 923 -> 2115 -> 4213', msg=f"dla zmiennych: Node(1, Node(3, Node(2, Node(123, Node(100, Node(23, Node(123, Node(923, Node(4213, Node(312, Node(2115))))))))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 23 -> 100 -> 123 -> 123 -> 312 -> 923 -> 2115 -> 4213'")

    def test_Nr04_selection_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = selection_sort(Node(1, Node(1, Node(1))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 1 -> 1', msg=f"dla zmiennych: Node(1, Node(1, Node(1))). Otrzymano: {wynik}, oczekiwano: '1 -> 1 -> 1'")

    def test_Nr05_selection_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = selection_sort(Node(2, Node(1)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2', msg=f"dla zmiennych: Node(2, Node(1)). Otrzymano: {wynik}, oczekiwano: '1 -> 2'")

    def test_Nr06_selection_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = selection_sort(Node(1, Node(2)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2', msg=f"dla zmiennych: Node(1, Node(2)). Otrzymano: {wynik}, oczekiwano: '1 -> 2'")

    def test_Nr07_selection_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = selection_sort(Node(1, Node(0)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0 -> 1', msg=f"dla zmiennych: Node(1, Node(0)). Otrzymano: {wynik}, oczekiwano: '0 -> 1'")

    def test_Nr08_selection_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = selection_sort(Node(0))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(0). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr09_selection_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = selection_sort(Node(123, Node(12312, Node(5123, Node(123, Node(213, Node(523, Node(23, Node(1, Node(123, Node(0, Node(231))))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0 -> 1 -> 23 -> 123 -> 123 -> 123 -> 213 -> 231 -> 523 -> 5123 -> 12312', msg=f"dla zmiennych: Node(123, Node(12312, Node(5123, Node(123, Node(213, Node(523, Node(23, Node(1, Node(123, Node(0, Node(231))))))))))). Otrzymano: {wynik}, oczekiwano: '0 -> 1 -> 23 -> 123 -> 123 -> 123 -> 213 -> 231 -> 523 -> 5123 -> 12312'")


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

