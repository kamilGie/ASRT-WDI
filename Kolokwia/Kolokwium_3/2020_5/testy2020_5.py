import unittest

from szablon2020_5 import Zadanie_5


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_5(self):
            self.assertEqual(Zadanie_5([2,4,6,7,8,10,12]), 0)

    def test_Nr02_Zadanie_5(self):
            self.assertEqual(Zadanie_5([2,3,4,6,7,8,10]), 1)

    def test_Nr03_Zadanie_5(self):
            self.assertEqual(Zadanie_5([2,4,3,6,5]), 2)

    def test_Nr04_Zadanie_5(self):
            self.assertEqual(Zadanie_5([2,3,4,5,6,8,7]), 5)

    def test_Nr05_Zadanie_5(self):
            self.assertEqual(Zadanie_5([2, 5, 8, 11, 13, 17, 19]), 13)

    def test_Nr06_Zadanie_5(self):
            self.assertEqual(Zadanie_5([2, 9, 15]), 0)

    def test_Nr07_Zadanie_5(self):
            self.assertEqual(Zadanie_5([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]), 28)

def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "Funkcja rekurencyjnie przechodzi po tablicy, sprawdzając różne kombinacje trójek, i dodaje do wyniku te, które spełniają warunki",
        "sprawdza, czy trzy liczby są parami względnie pierwsze i czy odległość między ich indeksami w tablicy nie przekracza 2",
        "Funkcja najpierw definiuje, kiedy liczby są parami względnie pierwsze za pomocą NWD. Następnie, rekurencyjnie idzie po tablicy, decydując, czy dodać aktualną liczbę do trójki. Sprawdza, czy odległość indeksów jest poprawna i czy trójka spełnia warunki. Jeśli warunki są spełnione, zwiększa licznik trójek. Proces trwa aż do przeanalizowania wszystkich możliwych kombinacji w tablicy."
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



