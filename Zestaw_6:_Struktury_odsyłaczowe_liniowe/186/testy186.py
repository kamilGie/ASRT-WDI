import unittest
from contextlib import redirect_stdout
import io

from szablon186 import Zadanie_186
from szablon186 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_186(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_186(Node("a",Node("b",Node("c"))),"c")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node("a",Node("b",Node("c"))),"c". Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr02_Zadanie_186(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_186(Node("apple"), "banana")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node("apple"), "banana". Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr03_Zadanie_186(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_186(Node("apple" ,Node( "cherry")), "banana")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node("apple" ,Node( "cherry")), "banana". Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr04_Zadanie_186(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_186(Node("apple" ,Node( "banana")), "apple")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node("apple" ,Node( "banana")), "apple". Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr05_Zadanie_186(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_186(Node("apple" ,Node( "banana" ,Node( "cherry"))), "date")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node("apple" ,Node( "banana" ,Node( "cherry"))), "date". Otrzymano: {wynik}, oczekiwano: 'True'")


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

