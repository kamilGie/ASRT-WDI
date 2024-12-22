import unittest
from contextlib import redirect_stdout
import io

from szablon195 import Zadanie_195
from szablon195 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(1 ,Node( 2 ,Node( 3 ,Node( 1 ,Node( 2 ,Node( 1)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 1', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 3 ,Node( 1 ,Node( 2 ,Node( 1)))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 1'")

    def test_Nr02_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(5 ,Node( 6 ,Node( 7 ,Node( 1 ,Node( 2 ,Node( 3 ,Node( 4))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 -> 6 -> 7', msg=f"dla zmiennych: Node(5 ,Node( 6 ,Node( 7 ,Node( 1 ,Node( 2 ,Node( 3 ,Node( 4))))))). Otrzymano: {wynik}, oczekiwano: '5 -> 6 -> 7'")

    def test_Nr03_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(5 ,Node( 6 ,Node( 7 ,Node( 1 ,Node( 2 ,Node( 3)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 -> 6 -> 7 -> 1 -> 2 -> 3', msg=f"dla zmiennych: Node(5 ,Node( 6 ,Node( 7 ,Node( 1 ,Node( 2 ,Node( 3)))))). Otrzymano: {wynik}, oczekiwano: '5 -> 6 -> 7 -> 1 -> 2 -> 3'")

    def test_Nr04_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(10 ,Node( 20 ,Node( 30 ,Node( 5 ,Node( 15 ,Node( 25 ,Node( 35))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10 -> 20 -> 30', msg=f"dla zmiennych: Node(10 ,Node( 20 ,Node( 30 ,Node( 5 ,Node( 15 ,Node( 25 ,Node( 35))))))). Otrzymano: {wynik}, oczekiwano: '10 -> 20 -> 30'")

    def test_Nr05_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(1 ,Node( 2 ,Node( 3 ,Node( 1 ,Node( 2 ,Node( 1)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 1', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 3 ,Node( 1 ,Node( 2 ,Node( 1)))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 1'")

    def test_Nr06_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(1 ,Node( 2 ,Node( 1))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 1))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr07_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(5 ,Node( 6 ,Node( 7 ,Node( 1 ,Node( 2 ,Node( 3 ,Node( 4))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 -> 6 -> 7', msg=f"dla zmiennych: Node(5 ,Node( 6 ,Node( 7 ,Node( 1 ,Node( 2 ,Node( 3 ,Node( 4))))))). Otrzymano: {wynik}, oczekiwano: '5 -> 6 -> 7'")

    def test_Nr08_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(5 ,Node( 6 ,Node( 7 ,Node( 1)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(5 ,Node( 6 ,Node( 7 ,Node( 1)))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr09_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(10 ,Node( 20 ,Node( 30 ,Node( 5 ,Node( 15 ,Node( 25 ,Node( 35))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10 -> 20 -> 30', msg=f"dla zmiennych: Node(10 ,Node( 20 ,Node( 30 ,Node( 5 ,Node( 15 ,Node( 25 ,Node( 35))))))). Otrzymano: {wynik}, oczekiwano: '10 -> 20 -> 30'")

    def test_Nr10_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(4 ,Node( 3 ,Node( 2 ,Node( 1 ,Node( 6 ,Node( 7 ,Node( 8))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4 -> 3 -> 2', msg=f"dla zmiennych: Node(4 ,Node( 3 ,Node( 2 ,Node( 1 ,Node( 6 ,Node( 7 ,Node( 8))))))). Otrzymano: {wynik}, oczekiwano: '4 -> 3 -> 2'")

    def test_Nr11_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(2 ,Node( 4 ,Node( 6 ,Node( 8 ,Node( 3 ,Node( 5 ,Node( 7))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3 -> 5 -> 7', msg=f"dla zmiennych: Node(2 ,Node( 4 ,Node( 6 ,Node( 8 ,Node( 3 ,Node( 5 ,Node( 7))))))). Otrzymano: {wynik}, oczekiwano: '3 -> 5 -> 7'")

    def test_Nr12_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(1 ,Node( 5 ,Node( 2 ,Node( 6 ,Node( 3 ,Node( 7 ,Node( 4))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4', msg=f"dla zmiennych: Node(1 ,Node( 5 ,Node( 2 ,Node( 6 ,Node( 3 ,Node( 7 ,Node( 4))))))). Otrzymano: {wynik}, oczekiwano: '1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4'")

    def test_Nr13_Zadanie_195(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_195(Node(1 ,Node( 5 ,Node( 2 ,Node( 6 ,Node( 3 ,Node( 7 ,Node( 4))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4', msg=f"dla zmiennych: Node(1 ,Node( 5 ,Node( 2 ,Node( 6 ,Node( 3 ,Node( 7 ,Node( 4))))))). Otrzymano: {wynik}, oczekiwano: '1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4'")


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

