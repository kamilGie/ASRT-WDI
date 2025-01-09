import unittest
from contextlib import redirect_stdout
import io

from szablon46 import Zadanie_46


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_46(self):
        self.assertEqual(Zadanie_46(0, 10000, 3), 19)

    def test_Nr02_Zadanie_46(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = Zadanie_46(50, 100, 4)
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "",
            msg=f"""dla zmiennych: 50,100,4. Otrzymano: {wynik}, oczekiwano: '' """,
        )

    def test_Nr03_Zadanie_46(self):
        self.assertEqual(Zadanie_46(50, 1000, 2), 97)

    def test_Nr04_Zadanie_46(self):
        self.assertEqual(Zadanie_46(1231, 3123, 3), 1373)

    def test_Nr05_Zadanie_46(self):
        self.assertEqual(Zadanie_46(1, 10, 1), 7)

    def test_Nr06_Zadanie_46(self):
        self.assertEqual(Zadanie_46(1, 3213321, 20), 383)

    def test_Nr07_Zadanie_46(self):
        self.assertEqual(Zadanie_46(123, 231, 1), 139)

    def test_Nr08_Zadanie_46(self):
        self.assertEqual(Zadanie_46(139, 140, 1), 139)

    def test_Nr09_Zadanie_46(self):
        self.assertEqual(Zadanie_46(139, 150, 1), 139)


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


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
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )
