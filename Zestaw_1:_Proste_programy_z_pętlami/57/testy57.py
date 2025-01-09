import unittest
from contextlib import redirect_stdout
import io

from szablon57 import Zadanie_57


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_57(self):
        self.assertEqual(Zadanie_57(16), 3)

    def test_Nr02_Zadanie_57(self):
        self.assertEqual(Zadanie_57(13), 4)

    def test_Nr03_Zadanie_57(self):
        self.assertEqual(Zadanie_57(26), 15)

    def test_Nr06_Zadanie_57(self):
        self.assertEqual(Zadanie_57(10), 7)

    def test_Nr07_Zadanie_57(self):
        self.assertEqual(Zadanie_57(21), 7)

    def test_Nr08_Zadanie_57(self):
        self.assertEqual(Zadanie_57(24), 13)

    def test_Nr09_Zadanie_57(self):
        self.assertEqual(Zadanie_57(17), 7)

    def test_Nr10_Zadanie_57(self):
        self.assertEqual(Zadanie_57(51), 7)

    def test_Nr12_Zadanie_57(self):
        self.assertEqual(Zadanie_57(19), 6)

    def test_Nr13_Zadanie_57(self):
        self.assertEqual(Zadanie_57(2), 3)

    def test_Nr14_Zadanie_57(self):
        self.assertEqual(Zadanie_57(541), 9)


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "While podstawy od 2 do 16 pierwsza znaleziona podstawe zwracamy",
        "Rotacja w lewo polega na przeniesieniu najbardziej znaczącej cyfry na koniec. Liczymy liczbę cyfr, wyznaczamy najbardziej znaczącą cyfrę przez dzielenie, usuwamy ją przez modulo, przesuwamy resztę w lewo przez mnożenie i dodajemy tę cyfrę na koniec.",
        "Iloczyn cyfr liczby w danej podstawie oblicza się, pobierając kolejne cyfry przez resztę z dzielenia (% podstawa), mnożąc je do iloczynu, i usuwając najmniej znaczącą cyfrę przez dzielenie całkowite (// podstawa). Jeśli iloczyn stanie się 0, pętla jest przerywana.",
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
