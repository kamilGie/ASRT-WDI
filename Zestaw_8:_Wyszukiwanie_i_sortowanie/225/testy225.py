import unittest

from szablon225 import Zadanie_225


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

    def test_Nr01_Zadanie_225(self):
            self.assertEqual(Zadanie_225([3,0,2,0,1]), [1, 0, 2, 0, 3])

    def test_Nr02_Zadanie_225(self):
            self.assertEqual(Zadanie_225([4, 3, 2, 1, 0, 0]), [1, 2, 3, 4, 0, 0])

    def test_Nr03_Zadanie_225(self):
            self.assertEqual(Zadanie_225([0, 0, 3, 1, 2]), [0, 0, 1, 2, 3])

    def test_Nr04_Zadanie_225(self):
            self.assertEqual(Zadanie_225([0, 0, 1, 1, 1]), [0, 0, 1, 1, 1])

    def test_Nr05_Zadanie_225(self):
            self.assertEqual(Zadanie_225([0, 100, 50, 0, 200]), [0, 50, 100, 0, 200])

    def test_Nr06_Zadanie_225(self):
            self.assertEqual(Zadanie_225([2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1]), [1, 0, 1, 0, 2, 0, 2, 0, 3, 0, 3])

    def test_Nr07_Zadanie_225(self):
            self.assertEqual(Zadanie_225([0] * 100 + [i for i in range(100, 0, -1)]), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])

    def test_Nr08_Zadanie_225(self):
            self.assertEqual(Zadanie_225([0, 1, 2, 0, 3, 4, 0, 5, 6]), [0, 1, 2, 0, 3, 4, 0, 5, 6])


