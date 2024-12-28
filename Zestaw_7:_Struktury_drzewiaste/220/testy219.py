import unittest
from contextlib import redirect_stdout
import io

from szablon219 import Zadanie_219
from szablon219 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_219(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_219(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr02_Zadanie_219(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_219(Node(20, Node(10, Node(5, None, Node(7)), Node(15)), Node(30, Node(25), Node(35))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(20, Node(10, Node(5, None, Node(7)), Node(15)), Node(30, Node(25), Node(35))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr03_Zadanie_219(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_219(Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13)))). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr04_Zadanie_219(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_219(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr06_Zadanie_219(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_219(Node(100, Node(50, None, Node(75)), Node(120)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(100, Node(50, None, Node(75)), Node(120)). Otrzymano: {wynik}, oczekiwano: '2'")


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

