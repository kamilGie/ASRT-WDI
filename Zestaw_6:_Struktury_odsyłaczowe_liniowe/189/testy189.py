import unittest
from contextlib import redirect_stdout
import io

from szablon189 import Zadanie_189
from szablon189 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(5 ,Node( 8 ,Node( 10 ,Node( 7 ,Node( 15))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 -> 8 -> 7 -> 15', msg=f"dla zmiennych: Node(5 ,Node( 8 ,Node( 10 ,Node( 7 ,Node( 15))))). Otrzymano: {wynik}, oczekiwano: '5 -> 8 -> 7 -> 15'")

    def test_Nr02_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(4 ,Node( 13 ,Node( 9 ,Node( 6)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '6', msg=f"dla zmiennych: Node(4 ,Node( 13 ,Node( 9 ,Node( 6)))). Otrzymano: {wynik}, oczekiwano: '6'")

    def test_Nr03_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(3 ,Node( 6 ,Node( 12 ,Node( 19 ,Node( 18))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '6 -> 19 -> 18', msg=f"dla zmiennych: Node(3 ,Node( 6 ,Node( 12 ,Node( 19 ,Node( 18))))). Otrzymano: {wynik}, oczekiwano: '6 -> 19 -> 18'")

    def test_Nr05_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(7 ,Node( 8 ,Node( 9 ,Node( 10 ,Node( 11))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '7 -> 8 -> 11', msg=f"dla zmiennych: Node(7 ,Node( 8 ,Node( 9 ,Node( 10 ,Node( 11))))). Otrzymano: {wynik}, oczekiwano: '7 -> 8 -> 11'")

    def test_Nr06_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(1 ,Node( 2 ,Node( 4 ,Node( 8 ,Node( 16))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2 -> 8', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 4 ,Node( 8 ,Node( 16))))). Otrzymano: {wynik}, oczekiwano: '2 -> 8'")

    def test_Nr07_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(2 ,Node( 4 ,Node( 16))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(2 ,Node( 4 ,Node( 16))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr08_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(5 ,Node( 7 ,Node( 11 ,Node( 13 ,Node( 17))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 -> 7 -> 11 -> 17', msg=f"dla zmiennych: Node(5 ,Node( 7 ,Node( 11 ,Node( 13 ,Node( 17))))). Otrzymano: {wynik}, oczekiwano: '5 -> 7 -> 11 -> 17'")

    def test_Nr09_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(14 ,Node( 21 ,Node( 28 ,Node( 35)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '21 -> 35', msg=f"dla zmiennych: Node(14 ,Node( 21 ,Node( 28 ,Node( 35)))). Otrzymano: {wynik}, oczekiwano: '21 -> 35'")

    def test_Nr10_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(25 ,Node( 30 ,Node( 40 ,Node( 50 ,Node( 60))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '25 -> 50 -> 60', msg=f"dla zmiennych: Node(25 ,Node( 30 ,Node( 40 ,Node( 50 ,Node( 60))))). Otrzymano: {wynik}, oczekiwano: '25 -> 50 -> 60'")

    def test_Nr11_Zadanie_189(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_189(Node(30 ,Node( 40 ,Node( 60))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '60', msg=f"dla zmiennych: Node(30 ,Node( 40 ,Node( 60))). Otrzymano: {wynik}, oczekiwano: '60'")


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

