import unittest
from contextlib import redirect_stdout
import io

from szablon201 import iteration, recursive
from szablon201 import Node

class testy(unittest.TestCase):

    def test_Nr01_iteration(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iteration(Node(1,Node(2,Node(3))),  Node(4,Node(5,Node(6))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6', msg=f"dla zmiennych: Node(1,Node(2,Node(3))),  Node(4,Node(5,Node(6))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6'")

    def test_Nr02_iteration(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iteration(Node(1), Node(1,Node(2,Node(3,Node(4,Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 1 -> 2 -> 3 -> 4 -> 5', msg=f"dla zmiennych: Node(1), Node(1,Node(2,Node(3,Node(4,Node(5))))). Otrzymano: {wynik}, oczekiwano: '1 -> 1 -> 2 -> 3 -> 4 -> 5'")

    def test_Nr03_iteration(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iteration( Node(1,Node(2,Node(3,Node(4,Node(5))))),Node(6))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6', msg=f"dla zmiennych:  Node(1,Node(2,Node(3,Node(4,Node(5))))),Node(6). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6'")

    def test_Nr04_iteration(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iteration(Node(1,Node(3,Node(5))),Node(2,Node(4,Node(6,Node(7,Node(8))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8', msg=f"dla zmiennych: Node(1,Node(3,Node(5))),Node(2,Node(4,Node(6,Node(7,Node(8))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8'")

    def test_Nr05_iteration(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iteration(Node(1,Node(4,Node(7))),Node(2,Node(3,Node(5,Node(6)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7', msg=f"dla zmiennych: Node(1,Node(4,Node(7))),Node(2,Node(3,Node(5,Node(6)))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7'")

    def test_Nr01_recursive(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = recursive(Node(1,Node(2,Node(3))),  Node(4,Node(5,Node(6))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6', msg=f"dla zmiennych: Node(1,Node(2,Node(3))),  Node(4,Node(5,Node(6))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6'")

    def test_Nr02_recursive(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = recursive(Node(1), Node(1,Node(2,Node(3,Node(4,Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 1 -> 2 -> 3 -> 4 -> 5', msg=f"dla zmiennych: Node(1), Node(1,Node(2,Node(3,Node(4,Node(5))))). Otrzymano: {wynik}, oczekiwano: '1 -> 1 -> 2 -> 3 -> 4 -> 5'")

    def test_Nr03_recursive(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = recursive(Node(1,Node(2,Node(3,Node(4,Node(5))))),Node(6))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6', msg=f"dla zmiennych: Node(1,Node(2,Node(3,Node(4,Node(5))))),Node(6). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6'")

    def test_Nr04_recursive(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = recursive(Node(1,Node(3,Node(5))),Node(2,Node(4,Node(6,Node(7,Node(8))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8', msg=f"dla zmiennych: Node(1,Node(3,Node(5))),Node(2,Node(4,Node(6,Node(7,Node(8))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8'")

    def test_Nr05_recursive(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = recursive(Node(1,Node(4,Node(7))),Node(2,Node(3,Node(5,Node(6)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7', msg=f"dla zmiennych: Node(1,Node(4,Node(7))),Node(2,Node(3,Node(5,Node(6)))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7'")


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

