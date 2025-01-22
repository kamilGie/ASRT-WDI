import unittest

from szablon2023_5B import thirteen


class testy(unittest.TestCase):

    def test_Nr01_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            True,
        )

    def test_Nr02_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            True,
        )

    def test_Nr03_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 11, 0, 11),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            False,
        )

    def test_Nr04_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 13, 0, 12),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            False,
        )

    def test_Nr05_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 121, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            False,
        )

    def test_Nr06_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 14, 0, 14),
                    (15, 29, 0, 14),
                    (30, 44, 0, 14),
                    (45, 59, 0, 14),
                    (0, 12, 15, 27),
                    (13, 25, 15, 27),
                    (26, 37, 28, 39),
                    (38, 49, 28, 39),
                    (0, 10, 40, 50),
                    (11, 21, 40, 50),
                    (22, 31, 51, 60),
                    (32, 41, 51, 60),
                    (42, 50, 61, 69),
                ]
            ),
            False,
        )

    def test_Nr07_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 23, 13, 36),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            False,
        )

    def test_Nr08_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (0, 6, 0, 6),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            True,
        )

    def test_Nr09_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (0, 6, 0, 6),
                    (12, 24, 0, 12),
                    (12, 30, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            True,
        )

    def test_Nr10_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            True,
        )

    def test_Nr11_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                ]
            ),
            False,
        )

    def test_Nr12_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (12, 24, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 1, 38, 39),
                    (1, 2, 38, 39),
                ]
            ),
            False,
        )

    def test_Nr13_thirteen(self):
        self.assertEqual(
            thirteen(
                [
                    (0, 12, 0, 12),
                    (10, 22, 0, 12),
                    (24, 36, 0, 12),
                    (36, 48, 0, 12),
                    (48, 60, 0, 12),
                    (60, 72, 0, 12),
                    (72, 84, 0, 12),
                    (84, 96, 0, 12),
                    (96, 108, 0, 12),
                    (108, 120, 0, 12),
                    (0, 24, 13, 37),
                    (0, 2, 38, 40),
                    (2, 4, 38, 40),
                ]
            ),
            False,
        )


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "Rekurencyjnie szukamy kombinacji 13 kwadratów, które nie nachodzą na siebie. Pętla kończy się, gdy mamy 13 elementów i pole wynosi 2024.",
        "Nachodzenie zachodzi, jeśli kwadrat nie leży całkowicie po lewej, prawej, poniżej lub powyżej drugiego.",
        "Tworzymy listę kwadratów rekurencyjnie. Gdy na liście jest 13 kwadratów, a szukane pole wynosi 0, zwracamy True. Jeśli doszliśmy do końca, lista kwadratów jest za duża lub pole jest za małe, zwracamy False. W tej rekurencyjnej funkcji, jeśli mamy mniej kwadratów i szukane pole jest większe, sprawdzamy, czy możemy dodać kwadrat, który nie nachodzi na żaden z istniejących. Jeśli można, dodajemy go do listy i kontynuujemy rekurencję.",
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
