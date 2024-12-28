import unittest

from szablon2023_3A import Zadanie_3A


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([7, 8, 6, 4, 7, 3]), 16.6)

    def test_Nr02_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([2, 3, 7, 11, 13]), 20.75)

    def test_Nr03_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([1009, 1013, 1021]), 0)

    def test_Nr04_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([1, 3, 5, 7]), 1.5)

    def test_Nr05_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([17, 19, 23, 29, 31]), 0)


    def test_Nr07_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([3, 7, 5, 11, 13]), 0)

    def test_Nr08_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([13, 17, 19, 23]), 0)

    def test_Nr09_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([4, 6, 7, 9, 11, 13, 15]), 41.75)

    def test_Nr10_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([31, 29, 23, 19, 17, 13]), 204.2)

    def test_Nr11_Zadanie_3A(self):
            self.assertEqual(Zadanie_3A([9, 10, 11, 13, 17]), 82.75)


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "Wyszukujemy wszystkie istniejące podciągi. Wyłączamy za pomocą edge case ciąg pełny, a dla wszystkich pozostałych wyliczamy 2 przypadki: kiedy zaczyna się dodawaniem i kiedy zaczyna się mnożeniem",
        "dla obu przypadków zerujemy niepierwsze wyniki i zwracamy wyższy",
        "Jeśli wynik > 0, znaczy że można wyznaczyć, iloraz, jeśli nie - znaczy dla tego podciągu nie ma rozwiązania spełniającego warunki zadania"
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



