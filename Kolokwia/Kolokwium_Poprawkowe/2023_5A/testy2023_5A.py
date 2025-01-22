import unittest
from contextlib import redirect_stdout
import io

from szablon2023_5A import square


class testy(unittest.TestCase):

    def test_Nr01_square(self):
            self.assertEqual(square([ [ 1 ,1 ,1] , [1,9,1],[1,1,1]]), 1)

    def test_Nr02_square(self):
            self.assertEqual(square([ [ 1 ,1 ,1] , [1,1,1],[1,1,1]]), 3)

    def test_Nr03_square(self):
            self.assertEqual(square([[8, 64, 9], [66, 1, 9], [8, 72, 8]]), 1)

    def test_Nr04_square(self):
            self.assertEqual(square([[8, 8, 8], [8, 8, 8], [8, 8, 8]]), 3)

    def test_Nr05_square(self):
            self.assertEqual(square([[1, 2, 3], [4, 5, 6], [7, 8, 7]]), 3)

    def test_Nr06_square(self):
            self.assertEqual(square([[1, 2, 3], [4, 5, 6], [7, 2, 7]]), 3)

    def test_Nr07_square(self):
            self.assertEqual(square([[1, 2, 3], [4, 5, 6], [7, 9, 7]]), 2)

    def test_Nr08_square(self):
            self.assertEqual(square([[10, 12, 8], [9, 64, 1], [2, 3, 5]]), 1)

    def test_Nr09_square(self):
            self.assertEqual(square([  [1, 2, 3],  [4, 5, 6],  [7, 8, 9]]), 2)

    def test_Nr10_square(self):
            self.assertEqual(square([  [9, 2, 3],  [4, 5, 6],  [7, 8, 1]]), 2)

    def test_Nr11_square(self):
            self.assertEqual(square([  [1, 2, 3],  [9, 5, 6],  [7, 8, 1]]), 2)

    def test_Nr12_square(self):
            self.assertEqual(square([  [1, 2, 9],  [1, 5, 6],  [7, 8, 1]]), 2)

    def test_Nr13_square(self):
            self.assertEqual(square([  [9, 9, 9],  [9, 9, 9],  [9, 9, 9]]), 0)

def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "stworzyc dodatowa tablice do przechowywania rozmiaru tablicy",
        "budowac kwadrat sprawdzajac gore lewo i prawa gore",
        "https://www.youtube.com/watch?v=nZAyRZC8tko"
    ]
    print(podpowiedzi[nr - 1])

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



