import unittest
from contextlib import redirect_stdout
import io

from szablon185 import Zadanie_185
from szablon185 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2,Node(3))),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 3', msg=f"dla zmiennych: Node(1,Node(2,Node(3))),2. Otrzymano: {wynik}, oczekiwano: '1 -> 3'")

    def test_Nr02_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2,Node(3))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2', msg=f"dla zmiennych: Node(1,Node(2,Node(3))),3. Otrzymano: {wynik}, oczekiwano: '1 -> 2'")

    def test_Nr03_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2,Node(3))),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2 -> 3', msg=f"dla zmiennych: Node(1,Node(2,Node(3))),1. Otrzymano: {wynik}, oczekiwano: '2 -> 3'")

    def test_Nr04_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2,Node(3))),4)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4 -> 1 -> 2 -> 3', msg=f"dla zmiennych: Node(1,Node(2,Node(3))),4. Otrzymano: {wynik}, oczekiwano: '4 -> 1 -> 2 -> 3'")

    def test_Nr05_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9,Node(10)))))))))),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 10', msg=f"dla zmiennych: Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9,Node(10)))))))))),5. Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 10'")

    def test_Nr06_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9,Node(10)))))))))),10)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9', msg=f"dla zmiennych: Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9,Node(10)))))))))),10. Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9'")

    def test_Nr07_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9,Node(10)))))))))),11)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '11 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10', msg=f"dla zmiennych: Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9,Node(10)))))))))),11. Otrzymano: {wynik}, oczekiwano: '11 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10'")

    def test_Nr08_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2)),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1,Node(2)),2. Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr09_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2)),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(1,Node(2)),1. Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr10_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1,Node(2)),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3 -> 1 -> 2', msg=f"dla zmiennych: Node(1,Node(2)),3. Otrzymano: {wynik}, oczekiwano: '3 -> 1 -> 2'")

    def test_Nr11_Zadanie_185(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_185(Node(1),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2 -> 1', msg=f"dla zmiennych: Node(1),2. Otrzymano: {wynik}, oczekiwano: '2 -> 1'")


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

