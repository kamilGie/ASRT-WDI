import unittest

from szablon2022_B5 import repair


class testy(unittest.TestCase):

    def test_Nr01_repair(self):
        self.assertEqual(
            repair(
                [
                    [8, 1, 2, 7, 5, 3, 6, 4, 9],
                    [9, 4, 3, 6, 8, 2, 1, 7, 5],
                    [6, 7, 5, 4, 9, 1, 2, 8, 3],
                    [1, 5, 4, 3, 6, 8, 8, 9, 6],
                    [3, 6, 9, 9, 1, 7, 7, 2, 1],
                    [2, 8, 7, 4, 5, 2, 5, 3, 4],
                    [5, 2, 1, 9, 7, 4, 2, 3, 7],
                    [4, 3, 8, 5, 2, 6, 8, 4, 5],
                    [7, 9, 6, 3, 1, 8, 1, 6, 9],
                ]
            ),
            True,
        )

    def test_Nr02_repair(self):
        self.assertEqual(
            repair(
                [
                    [6, 7, 8, 5, 3, 4, 9, 1, 2],
                    [1, 9, 5, 6, 7, 2, 3, 4, 8],
                    [3, 4, 2, 1, 9, 8, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ]
            ),
            False,
        )

    def test_Nr03_repair(self):
        self.assertEqual(
            repair(
                [
                    [5, 3, 4, 6, 7, 8, 7, 6, 1],
                    [6, 7, 2, 1, 9, 5, 8, 5, 3],
                    [1, 9, 8, 3, 4, 2, 9, 2, 4],
                    [8, 5, 9, 9, 1, 2, 4, 2, 3],
                    [4, 2, 6, 3, 4, 8, 7, 9, 1],
                    [7, 1, 3, 5, 6, 7, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ]
            ),
            True,
        )

    def test_Nr04_repair(self):
        self.assertEqual(
            repair(
                [
                    [9, 1, 2, 4, 5, 6, 7, 8, 9],
                    [3, 4, 5, 7, 8, 9, 1, 2, 3],
                    [6, 7, 8, 1, 2, 3, 4, 5, 6],
                    [2, 3, 4, 5, 6, 7, 8, 9, 1],
                    [5, 6, 7, 8, 9, 1, 2, 3, 4],
                    [8, 9, 1, 2, 3, 4, 5, 6, 7],
                    [3, 4, 5, 6, 7, 8, 1, 2, 3],
                    [6, 7, 8, 9, 1, 2, 4, 5, 6],
                    [9, 1, 2, 3, 4, 5, 7, 8, 9],
                ]
            ),
            False,
        )

    def test_Nr05_repair(self):
        self.assertEqual(
            repair(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 2, 8, 4, 5, 3, 7],
                    [2, 8, 7, 6, 3, 5, 4, 1, 9],
                    [3, 4, 5, 1, 7, 9, 2, 8, 6],
                ]
            ),
            False,
        )


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "Brute force: zamieniam każdy kwadrat z każdym.",
        "Zamiana działa w ten sposób, że tworzę 9-elementową tablicę pozycji w kwadracie, np. (0,0), (0,1)... i dla każdej z tych pozycji zamieniam dwa małe kwadraty przekazane jako parametry do funkcji zamiany.",
        "Po zamianie kwadratów sprawdzam, czy w którymkolwiek wierszu lub kolumnie nie wystąpiła dana wartość więcej niż raz.",
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
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )
