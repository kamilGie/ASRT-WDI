import unittest
from contextlib import redirect_stdout
import io

from szablon216 import Zadanie_216
from szablon216 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr02_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(1, Node(2, Node(4, Node(7), Node(3)), Node(5)), Node(6, Node(8, Node(10), Node(9)), None)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(1, Node(2, Node(4, Node(7), Node(3)), Node(5)), Node(6, Node(8, Node(10), Node(9)), None)). Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr03_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(5, Node(3, Node(2), Node(4)), Node(8, Node(7), Node(10))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(5, Node(3, Node(2), Node(4)), Node(8, Node(7), Node(10))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr04_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(21, Node(13, Node(2), Node(19)), Node(44, Node(28), None)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(21, Node(13, Node(2), Node(19)), Node(44, Node(28), None)). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr05_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(2, Node(4, Node(8, Node(1), Node(3)), Node(6)), Node(5)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(2, Node(4, Node(8, Node(1), Node(3)), Node(6)), Node(5)). Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr06_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr07_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(42, Node(21, Node(10), Node(32)), Node(50)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(42, Node(21, Node(10), Node(32)), Node(50)). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr08_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(3, Node(2), Node(4, Node(1), Node(5))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(3, Node(2), Node(4, Node(1), Node(5))). Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr09_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(21, Node(13, Node(2), Node(19)), Node(44, Node(28), None)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(21, Node(13, Node(2), Node(19)), Node(44, Node(28), None)). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr10_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(15, Node(10, Node(5), Node(12)), Node(20, Node(18), Node(25))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(15, Node(10, Node(5), Node(12)), Node(20, Node(18), Node(25))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr11_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(60, Node(30, Node(15), Node(45, Node(40), Node(55))), Node(90, Node(75), None)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(60, Node(30, Node(15), Node(45, Node(40), Node(55))), Node(90, Node(75), None)). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr12_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(1, Node(2, Node(4, Node(7), Node(3)), Node(5)), Node(6, Node(8, Node(10), Node(9)), None)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(1, Node(2, Node(4, Node(7), Node(3)), Node(5)), Node(6, Node(8, Node(10), Node(9)), None)). Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr13_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(7, Node(3, Node(1), Node(8, Node(5), Node(2))), Node(4, Node(6), None)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(7, Node(3, Node(1), Node(8, Node(5), Node(2))), Node(4, Node(6), None)). Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr14_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(25, Node(15, Node(10), Node(20)), Node(35, Node(30), Node(40))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(25, Node(15, Node(10), Node(20)), Node(35, Node(30), Node(40))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr15_Zadanie_216(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_216(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)). Otrzymano: {wynik}, oczekiwano: 'True'")


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

