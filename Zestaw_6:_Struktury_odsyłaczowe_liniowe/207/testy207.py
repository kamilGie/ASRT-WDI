import unittest
from contextlib import redirect_stdout
import io

from szablon207 import Zadanie_207
from szablon207 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_207(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_207((lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"ewa")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: (lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"ewa". Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr02_Zadanie_207(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_207((lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"adam")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: (lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"adam". Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr03_Zadanie_207(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_207(Node("bartek", Node("leszek", Node("marek", Node("ola", Node("zosia", Node("bartek")))))),"zuza")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node("bartek", Node("leszek", Node("marek", Node("ola", Node("zosia", Node("bartek")))))),"zuza". Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr04_Zadanie_207(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_207((lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"zzz")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: (lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"zzz". Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr05_Zadanie_207(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_207((lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"az")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: (lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"az". Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr06_Zadanie_207(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_207((lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"za")
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: (lambda n: (setattr(n, 'next', Node("leszek", Node("marek", Node("ola", Node( "zosia" ,n))))), n)[1])(Node("bartek")),"za". Otrzymano: {wynik}, oczekiwano: 'True'")


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

