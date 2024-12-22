import unittest
from contextlib import redirect_stdout
import io

from szablon176 import set_value, get_value, initialize_set
from szablon176 import Node

class testy(unittest.TestCase):

    def test_Nr01_set_value(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = set_value(Node([2,5],Node([6, 8] ,Node( [9, 3]))),4,4)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[2, 5] -> (4, 4) -> [6, 8] -> [9, 3]', msg=f"dla zmiennych: {str(Node([2,5],Node([6, 8] ,Node( [9, 3])))),4,4}. Otrzymano: {wynik}, oczekiwano: '[2, 5] -> (4, 4) -> [6, 8] -> [9, 3]'")

    def test_Nr02_set_value(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = set_value(Node([2,5],Node([6, 8] ,Node( [9, 3]))),1,4)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '(1, 4) -> [2, 5] -> [6, 8] -> [9, 3]', msg=f"dla zmiennych: Node([2,5],Node([6, 8] ,Node( [9, 3]))),1,4. Otrzymano: {wynik}, oczekiwano: '(1, 4) -> [2, 5] -> [6, 8] -> [9, 3]'")

    def test_Nr03_set_value(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = set_value(Node([2,5],Node([6, 8] ,Node( [9, 3]))),2,None)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[6, 8] -> [9, 3]', msg=f"dla zmiennych: Node([2,5],Node([6, 8] ,Node( [9, 3]))),2,None. Otrzymano: {wynik}, oczekiwano: '[6, 8] -> [9, 3]'")

    def test_Nr04_set_value(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = set_value(Node([2,5],Node([6, 8] ,Node( [9, 3]))),2,2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '(2, 2) -> [6, 8] -> [9, 3]', msg=f"dla zmiennych: Node([2,5],Node([6, 8] ,Node( [9, 3]))),2,2. Otrzymano: {wynik}, oczekiwano: '(2, 2) -> [6, 8] -> [9, 3]'")

    def test_Nr01_get_value(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = get_value(Node([2,5],Node([6, 8] ,Node( [9, 3]))),9)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: {str(Node([2,5],Node([6, 8] ,Node( [9, 3])))),9}. Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr02_get_value(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = get_value(Node([2,5],Node([6, 8] ,Node( [9, 3]))),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node([2,5],Node([6, 8] ,Node( [9, 3]))),2. Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr03_get_value(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = get_value(Node([2,5],Node([6, 8] ,Node( [9, 3]))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '8', msg=f"dla zmiennych: Node([2,5],Node([6, 8] ,Node( [9, 3]))),6. Otrzymano: {wynik}, oczekiwano: '8'")

    def test_Nr04_get_value(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = get_value(Node([2,5],Node([6, 8] ,Node( [9, 3]))),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '', msg=f"dla zmiennych: Node([2,5],Node([6, 8] ,Node( [9, 3]))),1. Otrzymano: {wynik}, oczekiwano: ''")

    def test_Nr05_get_value(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = get_value(Node([2,5],Node([6, 8] ,Node( [9, 3]))),11)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '', msg=f"dla zmiennych: Node([2,5],Node([6, 8] ,Node( [9, 3]))),11. Otrzymano: {wynik}, oczekiwano: ''")

    def test_Nr01_initialize_set(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = initialize_set(Node(None,Node(None,Node(3,Node(None)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '(2, 3)', msg=f"dla zmiennych: Node(None,Node(None,Node(3,Node(None)))). Otrzymano: {wynik}, oczekiwano: '(2, 3)'")

    def test_Nr02_initialize_set(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = initialize_set(Node(1,Node(2,Node(3))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '(0, 1) -> (1, 2) -> (2, 3)', msg=f"dla zmiennych: Node(1,Node(2,Node(3))). Otrzymano: {wynik}, oczekiwano: '(0, 1) -> (1, 2) -> (2, 3)'")

    def test_Nr03_initialize_set(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = initialize_set(Node(1,Node(2,Node(None,Node(4,Node(5,Node(None)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '(0, 1) -> (1, 2) -> (3, 4) -> (4, 5)', msg=f"dla zmiennych: Node(1,Node(2,Node(None,Node(4,Node(5,Node(None)))))). Otrzymano: {wynik}, oczekiwano: '(0, 1) -> (1, 2) -> (3, 4) -> (4, 5)'")

    def test_Nr04_initialize_set(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = initialize_set(Node(None,Node(1,Node(None))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '(1, 1)', msg=f"dla zmiennych: Node(None,Node(1,Node(None))). Otrzymano: {wynik}, oczekiwano: '(1, 1)'")

    def test_Nr05_initialize_set(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = initialize_set(Node(1,Node(2,Node(3,Node(None)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '(0, 1) -> (1, 2) -> (2, 3)', msg=f"dla zmiennych: Node(1,Node(2,Node(3,Node(None)))). Otrzymano: {wynik}, oczekiwano: '(0, 1) -> (1, 2) -> (2, 3)'")

    def test_Nr06_initialize_set(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = initialize_set(Node(None,Node(1,Node(None,Node(None)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '(1, 1)', msg=f"dla zmiennych: Node(None,Node(1,Node(None,Node(None)))). Otrzymano: {wynik}, oczekiwano: '(1, 1)'")


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

