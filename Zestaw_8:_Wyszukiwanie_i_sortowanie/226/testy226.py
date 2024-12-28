import unittest

from szablon226 import Zadanie_226


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


class testy(unittest.TestCase):
   """ testy do tego sa bardzo skromne bo jest wiele poprawnych rozwiazań """
    def test_Nr01_Zadanie_226(self):
            tablica = [(2, 3, 1, 4), (3, 2, 4, 1), (1, 2, 3, 4), (1, 3, 4, 2)]
            Zadanie_226(tablica)
            self.assertEqual(tablica, [(1, 2, 3, 4), (1, 3, 4, 2), (2, 3, 1, 4), (3, 2, 4, 1)])

    def test_Nr02_Zadanie_226(self):
            tablica = [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4)]
            Zadanie_226(tablica)
            self.assertEqual(tablica, [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4)])

    def test_Nr03_Zadanie_226(self):
            tablica = [(1, 3, 2, 4), (1, 2, 4, 3), (1, 2, 3, 4)]
            Zadanie_226(tablica)
            self.assertEqual(tablica, [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4)])

