import unittest
from contextlib import redirect_stdout
import io

from szablon217 import Zadanie_217_rek, Zadanie_217_iter
from szablon217 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_217_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),5. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr02_Zadanie_217_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),7)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),7. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr03_Zadanie_217_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),10)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),10. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr04_Zadanie_217_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3. Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr05_Zadanie_217_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),5. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr06_Zadanie_217_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),1. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr07_Zadanie_217_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6. Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr08_Zadanie_217_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_rek(Node(500, Node(200, Node(100, Node(50), Node(150)), Node(300, Node(250), Node(350))), Node(800)),350)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(500, Node(200, Node(100, Node(50), Node(150)), Node(300, Node(250), Node(350))), Node(800)),350. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr09_Zadanie_217_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_rek(Node(500, Node(200, Node(100, Node(50), Node(150)), Node(300, Node(250), Node(350))), Node(800)),420)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(500, Node(200, Node(100, Node(50), Node(150)), Node(300, Node(250), Node(350))), Node(800)),420. Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr01_Zadanie_217_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),5. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr02_Zadanie_217_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),7)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),7. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr03_Zadanie_217_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),10)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),10. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr04_Zadanie_217_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3. Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr05_Zadanie_217_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),5. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr06_Zadanie_217_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),1. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr07_Zadanie_217_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6. Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr08_Zadanie_217_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_iter(Node(500, Node(200, Node(100, Node(50), Node(150)), Node(300, Node(250), Node(350))), Node(800)),350)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(500, Node(200, Node(100, Node(50), Node(150)), Node(300, Node(250), Node(350))), Node(800)),350. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr09_Zadanie_217_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_217_iter(Node(500, Node(200, Node(100, Node(50), Node(150)), Node(300, Node(250), Node(350))), Node(800)),420)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(500, Node(200, Node(100, Node(50), Node(150)), Node(300, Node(250), Node(350))), Node(800)),420. Otrzymano: {wynik}, oczekiwano: 'False'")


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

