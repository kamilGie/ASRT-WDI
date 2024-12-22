import unittest
from contextlib import redirect_stdout
import io

from szablon203 import Zadanie_203
from szablon203 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_203(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_203( Node(1 ,Node( 5 ,Node( 6 ,Node( 10 ,Node( 12))))),Node(2 ,Node( 3 ,Node( 5 ,Node( 10)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych:  Node(1 ,Node( 5 ,Node( 6 ,Node( 10 ,Node( 12))))),Node(2 ,Node( 3 ,Node( 5 ,Node( 10)))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr02_Zadanie_203(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_203(Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 9,Node(11)))))),Node(2 ,Node( 4 ,Node( 6 ,Node( 8 ,Node( 10,Node(11)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10', msg=f"dla zmiennych: Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 9,Node(11)))))),Node(2 ,Node( 4 ,Node( 6 ,Node( 8 ,Node( 10,Node(11)))))). Otrzymano: {wynik}, oczekiwano: '10'")

    def test_Nr03_Zadanie_203(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_203(Node(1 ,Node( 2 ,Node( 3 ,Node( 4 ,Node( 5))))),Node(1 ,Node( 2 ,Node( 3 ,Node( 4 ,Node( 5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(1 ,Node( 2 ,Node( 3 ,Node( 4 ,Node( 5))))),Node(1 ,Node( 2 ,Node( 3 ,Node( 4 ,Node( 5))))). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr04_Zadanie_203(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_203(Node(1 ,Node( 5 ,Node( 9 ,Node( 11)))),Node(5 ,Node( 7 ,Node( 9 ,Node( 13)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(1 ,Node( 5 ,Node( 9 ,Node( 11)))),Node(5 ,Node( 7 ,Node( 9 ,Node( 13)))). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr05_Zadanie_203(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_203( Node(1 ,Node( 2 ,Node( 3 ,Node( 4,Node(5))))),Node(5 ,Node( 6 ,Node( 7 ,Node( 8)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '7', msg=f"dla zmiennych:  Node(1 ,Node( 2 ,Node( 3 ,Node( 4,Node(5))))),Node(5 ,Node( 6 ,Node( 7 ,Node( 8)))). Otrzymano: {wynik}, oczekiwano: '7'")

    def test_Nr06_Zadanie_203(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_203(Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 9 ,Node( 11 ,Node( 13 ,Node( 15 ,Node( 17 ,Node( 19)))))))))),Node(5 ,Node( 15)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '8', msg=f"dla zmiennych: Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 9 ,Node( 11 ,Node( 13 ,Node( 15 ,Node( 17 ,Node( 19)))))))))),Node(5 ,Node( 15)). Otrzymano: {wynik}, oczekiwano: '8'")

    def test_Nr07_Zadanie_203(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_203(Node(5 ,Node( 15)),Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 9 ,Node( 11 ,Node( 13 ,Node( 15 ,Node( 17 ,Node( 19)))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '8', msg=f"dla zmiennych: Node(5 ,Node( 15)),Node(1 ,Node( 3 ,Node( 5 ,Node( 7 ,Node( 9 ,Node( 11 ,Node( 13 ,Node( 15 ,Node( 17 ,Node( 19)))))))))). Otrzymano: {wynik}, oczekiwano: '8'")


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

