import unittest
from contextlib import redirect_stdout
import io

from szablon2021_5 import three


class testy(unittest.TestCase):

    def test_Nr01_three(self):
        self.assertEqual(three([[14, 24, 14], [24, 24, 24], [24, 24, 14]]), 1)

    def test_Nr02_three(self):
        self.assertEqual(three([[2, 3, 5], [7, 6, 9], [10, 15, 14]]), 1)

    def test_Nr03_three(self):
        self.assertEqual(three([[24, 14, 35], [12, 18, 16], [21, 27, 49]]), 0)

    def test_Nr04_three(self):
        self.assertEqual(three([[6, 10, 15], [14, 21, 35], [33, 42, 77]]), 0)

    def test_Nr05_three(self):
        self.assertEqual(three([[8, 16, 32], [9, 27, 81], [5, 10, 20]]), 0)

    def test_Nr06_three(self):
        self.assertEqual(three([[4, 6, 9], [25, 30, 35], [49, 50, 55]]), 1)

    def test_Nr07_three(self):
        self.assertEqual(
            three(
                [
                    [24, 14, 35, 50, 15],
                    [12, 18, 16, 30, 21],
                    [21, 27, 49, 32, 40],
                    [14, 20, 25, 45, 28],
                    [10, 15, 20, 25, 30],
                ]
            ),
            1,
        )

    def test_Nr08_three(self):
        self.assertEqual(
            three(
                [
                    [2, 3, 5, 7, 11, 13],
                    [4, 6, 10, 14, 22, 26],
                    [8, 12, 18, 20, 28, 32],
                    [16, 24, 36, 40, 42, 48],
                    [32, 48, 54, 60, 66, 70],
                    [64, 72, 84, 90, 98, 100],
                ]
            ),
            3,
        )

    def test_Nr09_three(self):
        self.assertEqual(
            three(
                [
                    [6, 10, 14, 18, 22, 26, 30],
                    [15, 21, 33, 35, 39, 42, 45],
                    [28, 36, 44, 49, 55, 63, 66],
                    [25, 32, 40, 48, 56, 64, 72],
                    [27, 34, 41, 50, 57, 65, 73],
                    [30, 35, 42, 49, 54, 60, 68],
                    [36, 40, 48, 56, 64, 72, 80],
                ]
            ),
            7,
        )

    def test_Nr10_three(self):
        self.assertEqual(
            three(
                [
                    [8, 16, 32, 64, 128, 256, 512, 1024],
                    [3, 6, 12, 24, 48, 96, 192, 384],
                    [5, 10, 20, 40, 80, 160, 320, 640],
                    [7, 14, 28, 56, 112, 224, 448, 896],
                    [9, 18, 36, 72, 144, 288, 576, 1152],
                    [11, 22, 44, 88, 176, 352, 704, 1408],
                    [13, 26, 52, 104, 208, 416, 832, 1664],
                    [15, 30, 60, 120, 240, 480, 960, 1920],
                ]
            ),
            1,
        )

    def test_Nr11_three(self):
        self.assertEqual(
            three(
                [
                    [24, 36, 48, 60, 72, 84, 96, 108, 120],
                    [30, 45, 60, 75, 90, 105, 120, 135, 150],
                    [40, 50, 60, 70, 80, 90, 100, 110, 120],
                    [18, 27, 36, 45, 54, 63, 72, 81, 90],
                    [14, 28, 42, 56, 70, 84, 98, 112, 126],
                    [12, 24, 36, 48, 60, 72, 84, 96, 108],
                    [20, 30, 40, 50, 60, 70, 80, 90, 100],
                    [22, 44, 66, 88, 110, 132, 154, 176, 198],
                    [25, 50, 75, 100, 125, 150, 175, 200, 225],
                ]
            ),
            12,
        )


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "warunek sasiadow jest nietypowy i daje mozliwosci petli bez sprawdzania czy sasiad jest po za granicami",
        "Aby stwierdzić, czy dwie liczby są czynnikowo-podobne, obie muszą mieć dokładnie jeden wspólny czynnik pierwszy. Przejdź przez wszystkie liczby od 2 wzwyż i sprawdzaj, czy są dzielnikami obu liczb. Jeśli znajdziesz więcej niż jeden wspólny czynnik, przestań sprawdzać.",
        "Dla każdego czynnika n, sprawdzaj, czy jest dzielnikiem a; jeśli tak, dziel a przez n, aż przestanie być podzielna – to sprawdza, czy n jest czynnikiem pierwszym a; następnie sprawdzaj, czy n jest także dzielnikiem b. przejdz do nastepnego n rob tak az a jest wieksze od 0",
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
