import unittest
from contextlib import redirect_stdout
import io

from szablon190 import Zadanie_190
from szablon190 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(5, Node(10)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10 -> 5', msg=f"dla zmiennych: Node(5, Node(10)). Otrzymano: {wynik}, oczekiwano: '10 -> 5'")

    def test_Nr02_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(1, Node(2, Node(5, Node(6)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '6 -> 2 -> 1 -> 5', msg=f"dla zmiennych: Node(1, Node(2, Node(5, Node(6)))). Otrzymano: {wynik}, oczekiwano: '6 -> 2 -> 1 -> 5'")

    def test_Nr03_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(25, Node(45, Node(6, Node(125, Node(8))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '8 -> 6 -> 45 -> 25 -> 125', msg=f"dla zmiennych: Node(25, Node(45, Node(6, Node(125, Node(8))))). Otrzymano: {wynik}, oczekiwano: '8 -> 6 -> 45 -> 25 -> 125'")

    def test_Nr04_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(5, Node(55, Node(555, Node(5555)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5555 -> 55 -> 5 -> 555', msg=f"dla zmiennych: Node(5, Node(55, Node(555, Node(5555)))). Otrzymano: {wynik}, oczekiwano: '5555 -> 55 -> 5 -> 555'")

    def test_Nr05_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(5, Node(15, Node(25, Node(35, Node(45))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '45 -> 35 -> 25 -> 15 -> 5', msg=f"dla zmiennych: Node(5, Node(15, Node(25, Node(35, Node(45))))). Otrzymano: {wynik}, oczekiwano: '45 -> 35 -> 25 -> 15 -> 5'")

    def test_Nr06_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(45, Node(25, Node(5, Node(15, Node(35))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '35 -> 15 -> 25 -> 45 -> 5', msg=f"dla zmiennych: Node(45, Node(25, Node(5, Node(15, Node(35))))). Otrzymano: {wynik}, oczekiwano: '35 -> 15 -> 25 -> 45 -> 5'")

    def test_Nr07_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(77, Node(5, Node(99, Node(555)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '99 -> 77 -> 5 -> 555', msg=f"dla zmiennych: Node(77, Node(5, Node(99, Node(555)))). Otrzymano: {wynik}, oczekiwano: '99 -> 77 -> 5 -> 555'")

    def test_Nr08_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(123, Node(45, Node(8, Node(16, Node(255))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '255 -> 16 -> 8 -> 45 -> 123', msg=f"dla zmiennych: Node(123, Node(45, Node(8, Node(16, Node(255))))). Otrzymano: {wynik}, oczekiwano: '255 -> 16 -> 8 -> 45 -> 123'")

    def test_Nr09_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(45, Node(255, Node(123, Node(8, Node(16))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '16 -> 8 -> 123 -> 255 -> 45', msg=f"dla zmiennych: Node(45, Node(255, Node(123, Node(8, Node(16))))). Otrzymano: {wynik}, oczekiwano: '16 -> 8 -> 123 -> 255 -> 45'")

    def test_Nr10_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(8, Node(80, Node(88, Node(888)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '88 -> 80 -> 8 -> 888', msg=f"dla zmiennych: Node(8, Node(80, Node(88, Node(888)))). Otrzymano: {wynik}, oczekiwano: '88 -> 80 -> 8 -> 888'")

    def test_Nr11_Zadanie_190(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_190(Node(55, Node(25, Node(5, Node(35, Node(45, Node(555)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '45 -> 35 -> 25 -> 55 -> 5 -> 555', msg=f"dla zmiennych: Node(55, Node(25, Node(5, Node(35, Node(45, Node(555)))))). Otrzymano: {wynik}, oczekiwano: '45 -> 35 -> 25 -> 55 -> 5 -> 555'")


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

