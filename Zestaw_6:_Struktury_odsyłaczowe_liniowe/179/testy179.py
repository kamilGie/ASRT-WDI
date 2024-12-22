import unittest
from contextlib import redirect_stdout
import io

from szablon179 import Zadanie_179
from szablon179 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_179(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_179(Node(17, Node(3, Node(24, Node(15, Node(50, Node(101)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '50 -> 101 -> 3 -> 24 -> 15 -> 17', msg=f"dla zmiennych: Node(17, Node(3, Node(24, Node(15, Node(50, Node(101)))))). Otrzymano: {wynik}, oczekiwano: '50 -> 101 -> 3 -> 24 -> 15 -> 17'")

    def test_Nr02_Zadanie_179(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_179(Node(1, Node(12, Node(33, Node(44, Node(25, Node(26, Node(100, Node(7)))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '100 -> 1 -> 12 -> 33 -> 44 -> 25 -> 26 -> 7', msg=f"dla zmiennych: Node(1, Node(12, Node(33, Node(44, Node(25, Node(26, Node(100, Node(7)))))))). Otrzymano: {wynik}, oczekiwano: '100 -> 1 -> 12 -> 33 -> 44 -> 25 -> 26 -> 7'")

    def test_Nr03_Zadanie_179(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_179(Node(-1, Node(-12, Node(33, Node(52, Node(-73, Node(60)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '60 -> -1 -> -12 -> 52 -> 33 -> -73', msg=f"dla zmiennych: Node(-1, Node(-12, Node(33, Node(52, Node(-73, Node(60)))))). Otrzymano: {wynik}, oczekiwano: '60 -> -1 -> -12 -> 52 -> 33 -> -73'")

    def test_Nr04_Zadanie_179(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_179(Node(17, Node(3, Node(24, Node(15, Node(50, Node(101)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '50 -> 101 -> 3 -> 24 -> 15 -> 17', msg=f"dla zmiennych: Node(17, Node(3, Node(24, Node(15, Node(50, Node(101)))))). Otrzymano: {wynik}, oczekiwano: '50 -> 101 -> 3 -> 24 -> 15 -> 17'")

    def test_Nr05_Zadanie_179(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_179(Node(-1, Node(-12, Node(33, Node(52, Node(-73, Node(60)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '60 -> -1 -> -12 -> 52 -> 33 -> -73', msg=f"dla zmiennych: Node(-1, Node(-12, Node(33, Node(52, Node(-73, Node(60)))))). Otrzymano: {wynik}, oczekiwano: '60 -> -1 -> -12 -> 52 -> 33 -> -73'")

    def test_Nr06_Zadanie_179(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_179(Node(14, Node(2, Node(12, Node(21, Node(9, Node(99)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '21 -> 2 -> 12 -> 14 -> 9 -> 99', msg=f"dla zmiennych: Node(14, Node(2, Node(12, Node(21, Node(9, Node(99)))))). Otrzymano: {wynik}, oczekiwano: '21 -> 2 -> 12 -> 14 -> 9 -> 99'")

    def test_Nr07_Zadanie_179(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_179(Node(15, Node(25, Node(5, Node(45, Node(65, Node(85)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '15 -> 25 -> 5 -> 45 -> 65 -> 85', msg=f"dla zmiennych: Node(15, Node(25, Node(5, Node(45, Node(65, Node(85)))))). Otrzymano: {wynik}, oczekiwano: '15 -> 25 -> 5 -> 45 -> 65 -> 85'")


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

