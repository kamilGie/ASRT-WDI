import unittest
from contextlib import redirect_stdout
import io

from szablon188 import Zadanie_188
from szablon188 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_188(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_188(Node(1 ,Node( 2 ,Node( 4 ,Node( 8 ,Node( 3 ,Node( 6)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '8 -> 6', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 4 ,Node( 8 ,Node( 3 ,Node( 6)))))). Otrzymano: {wynik}, oczekiwano: '8 -> 6'")

    def test_Nr02_Zadanie_188(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_188(Node(2 ,Node( 4 ,Node( 8 ,Node( 16 ,Node( 5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '16 -> 5', msg=f"dla zmiennych: Node(2 ,Node( 4 ,Node( 8 ,Node( 16 ,Node( 5))))). Otrzymano: {wynik}, oczekiwano: '16 -> 5'")

    def test_Nr03_Zadanie_188(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_188(Node(3 ,Node( 6 ,Node( 9 ,Node( 12 ,Node( 15))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '6 -> 9 -> 12 -> 15', msg=f"dla zmiennych: Node(3 ,Node( 6 ,Node( 9 ,Node( 12 ,Node( 15))))). Otrzymano: {wynik}, oczekiwano: '6 -> 9 -> 12 -> 15'")

    def test_Nr04_Zadanie_188(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_188(Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 11))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3 -> 5 -> 7 -> 11', msg=f"dla zmiennych: Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 11))))). Otrzymano: {wynik}, oczekiwano: '3 -> 5 -> 7 -> 11'")

    def test_Nr05_Zadanie_188(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_188(Node(6 ,Node( 12 ,Node( 24 ,Node( 48 ,Node( 10))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '48 -> 10', msg=f"dla zmiennych: Node(6 ,Node( 12 ,Node( 24 ,Node( 48 ,Node( 10))))). Otrzymano: {wynik}, oczekiwano: '48 -> 10'")

    def test_Nr06_Zadanie_188(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_188(Node(5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10 -> 15 -> 20 -> 25', msg=f"dla zmiennych: Node(5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25))))). Otrzymano: {wynik}, oczekiwano: '10 -> 15 -> 20 -> 25'")

    def test_Nr07_Zadanie_188(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_188(Node(2 ,Node( 4 ,Node( 6 ,Node( 8 ,Node( 10))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4 -> 6 -> 8 -> 10', msg=f"dla zmiennych: Node(2 ,Node( 4 ,Node( 6 ,Node( 8 ,Node( 10))))). Otrzymano: {wynik}, oczekiwano: '4 -> 6 -> 8 -> 10'")

    def test_Nr08_Zadanie_188(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_188(Node(1 ,Node( 2 ,Node( 3 ,Node( 6 ,Node( 9 ,Node( 18)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2 -> 6 -> 18', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 3 ,Node( 6 ,Node( 9 ,Node( 18)))))). Otrzymano: {wynik}, oczekiwano: '2 -> 6 -> 18'")


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

