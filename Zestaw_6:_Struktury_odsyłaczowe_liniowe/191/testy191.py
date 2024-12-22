import unittest
from contextlib import redirect_stdout
import io

from szablon191 import Zadanie_191
from szablon191 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(3 ,Node( 5 ,Node( 6 ,Node( 9 ,Node( 12))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3 -> 5 -> 6 -> 9 -> 12', msg=f"dla zmiennych: Node(3 ,Node( 5 ,Node( 6 ,Node( 9 ,Node( 12))))). Otrzymano: {wynik}, oczekiwano: '3 -> 5 -> 6 -> 9 -> 12'")

    def test_Nr02_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(7 ,Node( 8 ,Node( 10 ,Node( 15 ,Node( 20))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10 -> 15 -> 20', msg=f"dla zmiennych: Node(7 ,Node( 8 ,Node( 10 ,Node( 15 ,Node( 20))))). Otrzymano: {wynik}, oczekiwano: '10 -> 15 -> 20'")


    def test_Nr05_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(2 ,Node( 4 ,Node( 8 ,Node( 16,Node(17))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '17', msg=f"dla zmiennych: Node(2 ,Node( 4 ,Node( 8 ,Node( 16,Node(17))))). Otrzymano: {wynik}, oczekiwano: '17'")


    def test_Nr07_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(31 ,Node( 14 ,Node( 7 ,Node( 28 ,Node( 3))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(31 ,Node( 14 ,Node( 7 ,Node( 28 ,Node( 3))))). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr08_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 -> 10 -> 15 -> 20', msg=f"dla zmiennych: Node(5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25))))). Otrzymano: {wynik}, oczekiwano: '5 -> 10 -> 15 -> 20'")

    def test_Nr10_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(9 ,Node( 18 ,Node( 27 ,Node( 36 ,Node( 45))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '9 -> 18 -> 27 -> 36 -> 45', msg=f"dla zmiennych: Node(9 ,Node( 18 ,Node( 27 ,Node( 36 ,Node( 45))))). Otrzymano: {wynik}, oczekiwano: '9 -> 18 -> 27 -> 36 -> 45'")

    def test_Nr11_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(11 ,Node( 22 ,Node( 33 ,Node( 44 ,Node( 55))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '33', msg=f"dla zmiennych: Node(11 ,Node( 22 ,Node( 33 ,Node( 44 ,Node( 55))))). Otrzymano: {wynik}, oczekiwano: '33'")

    def test_Nr12_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(21 ,Node( 42 ,Node( 63 ,Node( 84 ,Node( 105))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '63 -> 105', msg=f"dla zmiennych: Node(21 ,Node( 42 ,Node( 63 ,Node( 84 ,Node( 105))))). Otrzymano: {wynik}, oczekiwano: '63 -> 105'")

    def test_Nr13_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(3 ,Node( 5 ,Node( 6 ,Node( 9 ,Node( 12 ,Node( 15 ,Node( 18 ,Node( 21 ,Node( 24 ,Node( 27 ,Node( 30 ,Node( 33 ,Node( 36 ,Node( 39 ,Node( 42 ,Node( 45 ,Node( 48 ,Node( 51 ,Node( 54))))))))))))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3 -> 5 -> 6 -> 9 -> 12 -> 15 -> 18 -> 24 -> 27 -> 30 -> 33 -> 36 -> 39 -> 45 -> 48 -> 51 -> 54', msg=f"dla zmiennych: Node(3 ,Node( 5 ,Node( 6 ,Node( 9 ,Node( 12 ,Node( 15 ,Node( 18 ,Node( 21 ,Node( 24 ,Node( 27 ,Node( 30 ,Node( 33 ,Node( 36 ,Node( 39 ,Node( 42 ,Node( 45 ,Node( 48 ,Node( 51 ,Node( 54))))))))))))))))))). Otrzymano: {wynik}, oczekiwano: '3 -> 5 -> 6 -> 9 -> 12 -> 15 -> 18 -> 24 -> 27 -> 30 -> 33 -> 36 -> 39 -> 45 -> 48 -> 51 -> 54'")

    def test_Nr14_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25 ,Node( 30 ,Node( 35 ,Node( 40 ,Node( 45 ,Node( 50 ,Node( 55 ,Node( 60 ,Node( 65 ,Node( 70 ,Node( 75 ,Node( 80 ,Node( 85 ,Node( 90 ,Node( 95 ,Node( 100)))))))))))))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 -> 10 -> 15 -> 20 -> 30 -> 40 -> 45 -> 60 -> 65 -> 75 -> 80 -> 85 -> 90 -> 95', msg=f"dla zmiennych: Node(5 ,Node( 10 ,Node( 15 ,Node( 20 ,Node( 25 ,Node( 30 ,Node( 35 ,Node( 40 ,Node( 45 ,Node( 50 ,Node( 55 ,Node( 60 ,Node( 65 ,Node( 70 ,Node( 75 ,Node( 80 ,Node( 85 ,Node( 90 ,Node( 95 ,Node( 100)))))))))))))))))))). Otrzymano: {wynik}, oczekiwano: '5 -> 10 -> 15 -> 20 -> 30 -> 40 -> 45 -> 60 -> 65 -> 75 -> 80 -> 85 -> 90 -> 95'")

    def test_Nr15_Zadanie_191(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_191(Node(3 ,Node( 15 ,Node( 8 ,Node( 23 ,Node( 42 ,Node( 19 ,Node( 7 ,Node( 24 ,Node( 56 ,Node( 13 ,Node( 2 ,Node( 63 ,Node( 31 ,Node( 16 ,Node( 5 ,Node( 10 ,Node( 99 ,Node( 72 ,Node( 45 ,Node( 60 ,Node( 18 ,Node( 81 ,Node( 33 ,Node( 22)))))))))))))))))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3 -> 15 -> 23 -> 24 -> 63 -> 5 -> 10 -> 99 -> 72 -> 45 -> 60 -> 18 -> 33', msg=f"dla zmiennych: Node(3 ,Node( 15 ,Node( 8 ,Node( 23 ,Node( 42 ,Node( 19 ,Node( 7 ,Node( 24 ,Node( 56 ,Node( 13 ,Node( 2 ,Node( 63 ,Node( 31 ,Node( 16 ,Node( 5 ,Node( 10 ,Node( 99 ,Node( 72 ,Node( 45 ,Node( 60 ,Node( 18 ,Node( 81 ,Node( 33 ,Node( 22)))))))))))))))))))))))). Otrzymano: {wynik}, oczekiwano: '3 -> 15 -> 23 -> 24 -> 63 -> 5 -> 10 -> 99 -> 72 -> 45 -> 60 -> 18 -> 33'")


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

