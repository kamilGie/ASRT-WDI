import unittest
from contextlib import redirect_stdout
import io

from szablon206 import Zadanie_206
from szablon206 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_206(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_206(Node(1, Node(2, Node(3))),Node(1, Node(2, Node(2))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0 -> 0 -> 1', msg=f"dla zmiennych: Node(1, Node(2, Node(3))),Node(1, Node(2, Node(2))). Otrzymano: {wynik}, oczekiwano: '0 -> 0 -> 1'")

    def test_Nr02_Zadanie_206(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_206(Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(5, Node(6)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '-4 -> -4 -> 3 -> 4 -> 5', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(5, Node(6)). Otrzymano: {wynik}, oczekiwano: '-4 -> -4 -> 3 -> 4 -> 5'")

    def test_Nr03_Zadanie_206(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_206(Node(1),Node(5, Node(4, Node(3, Node(2, Node(1))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '-4 -> -4 -> -3 -> -2 -> -1', msg=f"dla zmiennych: Node(1),Node(5, Node(4, Node(3, Node(2, Node(1))))). Otrzymano: {wynik}, oczekiwano: '-4 -> -4 -> -3 -> -2 -> -1'")

    def test_Nr04_Zadanie_206(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_206(Node(9, Node(9, Node(9, Node(9, Node(9, Node(9)))))),Node(-1))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10 -> 9 -> 9 -> 9 -> 9 -> 9', msg=f"dla zmiennych: Node(9, Node(9, Node(9, Node(9, Node(9, Node(9)))))),Node(-1). Otrzymano: {wynik}, oczekiwano: '10 -> 9 -> 9 -> 9 -> 9 -> 9'")

    def test_Nr05_Zadanie_206(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_206(Node(5, Node(0, Node(5))),Node(3, Node(2, Node(1))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2 -> -2 -> 4', msg=f"dla zmiennych: Node(5, Node(0, Node(5))),Node(3, Node(2, Node(1))). Otrzymano: {wynik}, oczekiwano: '2 -> -2 -> 4'")

    def test_Nr06_Zadanie_206(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_206(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(6))))))),Node(1, Node(2, Node(9))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0 -> 0 -> -6 -> 4 -> 5 -> 6 -> 6', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(6))))))),Node(1, Node(2, Node(9))). Otrzymano: {wynik}, oczekiwano: '0 -> 0 -> -6 -> 4 -> 5 -> 6 -> 6'")


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

