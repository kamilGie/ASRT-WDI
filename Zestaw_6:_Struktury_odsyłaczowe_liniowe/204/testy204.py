import unittest
from contextlib import redirect_stdout
import io

from szablon204 import Zadanie_204
from szablon204 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_204(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_204(Node(2 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 11))))),Node(8 ,Node( 2 ,Node( 7 ,Node( 4)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 11', msg=f"dla zmiennych: Node(2 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 11))))),Node(8 ,Node( 2 ,Node( 7 ,Node( 4)))). Otrzymano: {wynik}, oczekiwano: '2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 11'")

    def test_Nr02_Zadanie_204(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_204(Node(1 ,Node( 2 ,Node( 3 ,Node( 6 ,Node( 9))))),Node(7 ,Node( 5 ,Node( 10 ,Node( 1)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 9 -> 10', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 3 ,Node( 6 ,Node( 9))))),Node(7 ,Node( 5 ,Node( 10 ,Node( 1)))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 9 -> 10'")

    def test_Nr03_Zadanie_204(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_204(Node(4 ,Node( 8 ,Node( 12))),Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 9))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 -> 12', msg=f"dla zmiennych: Node(4 ,Node( 8 ,Node( 12))),Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 9))))). Otrzymano: {wynik}, oczekiwano: '1 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 -> 12'")

    def test_Nr04_Zadanie_204(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_204(Node(1 ,Node( 2 ,Node( 3))),Node(4 ,Node( 5 ,Node( 6))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 3))),Node(4 ,Node( 5 ,Node( 6))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6'")

    def test_Nr05_Zadanie_204(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_204(Node(10 ,Node( 20 ,Node( 30 ,Node( 40)))),Node(5 ,Node( 15 ,Node( 25 ,Node( 35)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 -> 10 -> 15 -> 20 -> 25 -> 30 -> 35 -> 40', msg=f"dla zmiennych: Node(10 ,Node( 20 ,Node( 30 ,Node( 40)))),Node(5 ,Node( 15 ,Node( 25 ,Node( 35)))). Otrzymano: {wynik}, oczekiwano: '5 -> 10 -> 15 -> 20 -> 25 -> 30 -> 35 -> 40'")

    def test_Nr06_Zadanie_204(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_204(Node(2 ,Node( 4 ,Node( 6 ,Node( 8)))),Node(1 ,Node( 3 ,Node( 5 ,Node( 7)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8', msg=f"dla zmiennych: Node(2 ,Node( 4 ,Node( 6 ,Node( 8)))),Node(1 ,Node( 3 ,Node( 5 ,Node( 7)))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8'")

    def test_Nr07_Zadanie_204(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_204(Node(1 ,Node( 2 ,Node( 3))),Node(1 ,Node( 2 ,Node( 3))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 3))),Node(1 ,Node( 2 ,Node( 3))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3'")

    def test_Nr08_Zadanie_204(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_204(Node(1),Node(1 ,Node( 5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25 ,Node( 30))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 5 -> 10 -> 15 -> 20 -> 25 -> 30', msg=f"dla zmiennych: Node(1),Node(1 ,Node( 5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25 ,Node( 30))))))). Otrzymano: {wynik}, oczekiwano: '1 -> 5 -> 10 -> 15 -> 20 -> 25 -> 30'")

    def test_Nr09_Zadanie_204(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_204(Node(1 ,Node( 5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25 ,Node( 30))))))),Node(1))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 5 -> 10 -> 15 -> 20 -> 25 -> 30', msg=f"dla zmiennych: Node(1 ,Node( 5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25 ,Node( 30))))))),Node(1). Otrzymano: {wynik}, oczekiwano: '1 -> 5 -> 10 -> 15 -> 20 -> 25 -> 30'")


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

