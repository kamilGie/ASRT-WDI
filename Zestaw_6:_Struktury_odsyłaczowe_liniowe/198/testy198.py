import unittest
from contextlib import redirect_stdout
import io

from szablon198 import Zadanie_198
from szablon198 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_198(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_198(Node(1, (lambda n: (setattr(n, 'next', Node(3, n)), n)[1])(Node(2))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1, (lambda n: (setattr(n, 'next', Node(3, n)), n)[1])(Node(2))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr02_Zadanie_198(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_198(Node(1, Node(2, (lambda n: (setattr(n, 'next', Node(4, Node(5, n))), n)[1])(Node(3)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(1, Node(2, (lambda n: (setattr(n, 'next', Node(4, Node(5, n))), n)[1])(Node(3)))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr03_Zadanie_198(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_198(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, (lambda n: (setattr(n, 'next', Node(8, n)), n)[1])(Node(7)))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '6', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, (lambda n: (setattr(n, 'next', Node(8, n)), n)[1])(Node(7)))))))). Otrzymano: {wynik}, oczekiwano: '6'")

    def test_Nr04_Zadanie_198(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_198(Node(1, Node(2, Node(1, Node(2, Node(1, Node(2, Node(1, Node(2, (lambda n: (setattr(n, 'next', Node(2, n)), n)[1])(Node(1)))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '8', msg=f"dla zmiennych: Node(1, Node(2, Node(1, Node(2, Node(1, Node(2, Node(1, Node(2, (lambda n: (setattr(n, 'next', Node(2, n)), n)[1])(Node(1)))))))))). Otrzymano: {wynik}, oczekiwano: '8'")


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

