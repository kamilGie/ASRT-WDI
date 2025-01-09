import unittest

from szablon56 import Zadanie_56


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_56(self):
        self.assertEqual(Zadanie_56(1202742516), 251)

    def test_Nr02_Zadanie_56(self):
        self.assertEqual(Zadanie_56(123623471261), 62347)

    def test_Nr03_Zadanie_56(self):
        self.assertEqual(Zadanie_56(128578123), 8123)

    def test_Nr04_Zadanie_56(self):
        self.assertEqual(Zadanie_56(512783975), 5127839)

    def test_Nr05_Zadanie_56(self):
        self.assertEqual(Zadanie_56(17), 17)

    def test_Nr06_Zadanie_56(self):
        self.assertEqual(Zadanie_56(2115), 5)

    def test_Nr07_Zadanie_56(self):
        self.assertEqual(Zadanie_56(129057812), 29)

    def test_Nr08_Zadanie_56(self):
        self.assertEqual(Zadanie_56(569871), 9871)

    def test_Nr09_Zadanie_56(self):
        self.assertEqual(Zadanie_56(12351), 2351)

    def test_Nr10_Zadanie_56(self):
        self.assertEqual(Zadanie_56(122224451), 5)


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "Dwa zagnieżdżone fory: pierwszy iteruje po długości liczby, a drugi po długości liczby minus pierwszy.",
        "Cyfry z końca usuwa się, dzieląc przez 10 do potęgi odpowiadającej liczbie cyfr, którą chcemy usunąć. Cyfry z początku usuwa się, biorąc resztę z dzielenia przez 10 do potęgi liczby cyfr minus M.",
        "Aby sprawdzić, czy liczba ma unikalne cyfry bez użycia tablic, można zastosować własną notację lub użyć maski bitowej.",
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
