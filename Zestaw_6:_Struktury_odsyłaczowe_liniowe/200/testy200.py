import unittest
from contextlib import redirect_stdout
import io

from szablon200 import Zadanie_200
from szablon200 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(2, Node(3, Node(4))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(2, Node(3, Node(4))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr02_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(3, Node(4, Node(5))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(3, Node(4, Node(5))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr03_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(2, Node(3, Node(5))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(2, Node(3, Node(5))). Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr04_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(1, Node(2, Node(3))),Node(0, Node(1, Node(2, Node(3, Node(4, Node(5)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, Node(2, Node(3))),Node(0, Node(1, Node(2, Node(3, Node(4, Node(5)))))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr05_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(2, Node(2, Node(2, Node(2, Node(2, Node(1, Node(2, Node(2)))))))), Node(2, Node(1, Node(2))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(2, Node(2, Node(2, Node(2, Node(2, Node(1, Node(2, Node(2)))))))), Node(2, Node(1, Node(2))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr06_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(4, Node(5, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3))))))))))))))))),Node(1, Node(2, Node(3, Node(4, Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(4, Node(5, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3))))))))))))))))),Node(1, Node(2, Node(3, Node(4, Node(5))))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr07_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(4, Node(5, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3))))))))))))))))),Node(1, Node(2, Node(3))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(4, Node(5, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3))))))))))))))))),Node(1, Node(2, Node(3))). Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr08_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))),Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(4, Node(5, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3))))))))))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))),Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3, Node(4, Node(5, Node(1, Node(2, Node(3, Node(1, Node(2, Node(3))))))))))))))))). Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr09_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(2, Node(2, Node(2, Node(2, Node(2))))),Node(2, Node(2, Node(2, Node(2, Node(1))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(2, Node(2, Node(2, Node(2, Node(2))))),Node(2, Node(2, Node(2, Node(2, Node(1))))). Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr10_Zadanie_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_200(Node(1, Node(2, Node(3, Node(2, Node(1))))),Node(2, Node(3, Node(2))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(2, Node(1))))),Node(2, Node(3, Node(2))). Otrzymano: {wynik}, oczekiwano: 'True'")


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

