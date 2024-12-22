import unittest
from contextlib import redirect_stdout
import io

from szablon192 import Zadanie_192
from szablon192 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_192(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_192(Node(1 ,Node( 2 ,Node( 2 ,Node( 3 ,Node( 3 ,Node( 4)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 2 ,Node( 3 ,Node( 3 ,Node( 4)))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4'")

    def test_Nr02_Zadanie_192(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_192(Node(5 ,Node( 5 ,Node( 5 ,Node( 5)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(5 ,Node( 5 ,Node( 5 ,Node( 5)))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr03_Zadanie_192(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_192(Node(1 ,Node( 1 ,Node( 2 ,Node( 2 ,Node( 3 ,Node( 3)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3', msg=f"dla zmiennych: Node(1 ,Node( 1 ,Node( 2 ,Node( 2 ,Node( 3 ,Node( 3)))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3'")

    def test_Nr04_Zadanie_192(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_192(Node(10 ,Node( 20 ,Node( 30 ,Node( 20 ,Node( 40 ,Node( 50 ,Node( 10))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10 -> 20 -> 30 -> 40 -> 50', msg=f"dla zmiennych: Node(10 ,Node( 20 ,Node( 30 ,Node( 20 ,Node( 40 ,Node( 50 ,Node( 10))))))). Otrzymano: {wynik}, oczekiwano: '10 -> 20 -> 30 -> 40 -> 50'")

    def test_Nr05_Zadanie_192(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_192(Node(3 ,Node( 3 ,Node( 3 ,Node( 3 ,Node( 3 ,Node( 3)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(3 ,Node( 3 ,Node( 3 ,Node( 3 ,Node( 3 ,Node( 3)))))). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr06_Zadanie_192(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_192(Node(1 ,Node( 3 ,Node( 1 ,Node( 2 ,Node( 3 ,Node( 2 ,Node( 4))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 3 -> 2 -> 4', msg=f"dla zmiennych: Node(1 ,Node( 3 ,Node( 1 ,Node( 2 ,Node( 3 ,Node( 2 ,Node( 4))))))). Otrzymano: {wynik}, oczekiwano: '1 -> 3 -> 2 -> 4'")

    def test_Nr07_Zadanie_192(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_192(Node(1 ,Node( 3 ,Node( 2 ,Node( 4)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 3 -> 2 -> 4', msg=f"dla zmiennych: Node(1 ,Node( 3 ,Node( 2 ,Node( 4)))). Otrzymano: {wynik}, oczekiwano: '1 -> 3 -> 2 -> 4'")


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

