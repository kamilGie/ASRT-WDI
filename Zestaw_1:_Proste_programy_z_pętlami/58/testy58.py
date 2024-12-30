import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon58 import Zadanie_58


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


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
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_58_argumenty_(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_58()
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "370",
            "407",
            "153",
            "371",
            "8208",
            "1634",
            "9474",
            "93084",
            "92727",
            "54748",
            "548834",
            "9800817",
            "4210818",
            "1741725",
            "9926315",
            "24678050",
            "24678051",
            "88593477",
        }
        wynik_zbior = set(wynik.split())

        brakujace = ""
        dodatkowe = ""
        if wynik_zbior != oczekiwany_wynik:
            brakujace = oczekiwany_wynik - wynik_zbior
            dodatkowe = wynik_zbior - oczekiwany_wynik
            print("Brakujące w wynikach:", brakujace)
            print("Dodatkowe w wynikach:", dodatkowe)

        self.assertTrue(
            wynik_zbior == oczekiwany_wynik,
            f"Błąd: różnica zbiorów - brakujące: {brakujace}, dodatkowe: {dodatkowe}",
        )
