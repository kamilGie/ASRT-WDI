import unittest
from contextlib import redirect_stdout
import io

from szablon43 import Zadanie_43


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_43(self):
            self.assertEqual(Zadanie_43(216), 600)

    def test_Nr02_Zadanie_43(self):
            self.assertEqual(Zadanie_43(343), 700)

    def test_Nr03_Zadanie_43(self):
            self.assertEqual(Zadanie_43(81), 90)

    def test_Nr04_Zadanie_43(self):
            self.assertEqual(Zadanie_43(648), 666)

    def test_Nr05_Zadanie_43(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_43(1000)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '', msg=f"""dla zmiennych: 1000. Otrzymano: {wynik}, oczekiwano: '' """)

    def test_Nr06_Zadanie_43(self):
            self.assertEqual(Zadanie_43(6561), 9000)

def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "Wyznaczyć długość S na podstawie jej wartości i ustalić liczbę cyfr n.",
        "Iterować w dół od 10**n - 1 do 10**(n-1), aby sprawdzać liczby o dokładnie n cyfrach.",
        "Obliczać sumę n-tych potęg cyfr każdej liczby i porównywać z S. Jeśli suma się zgadza, zwrócić pierwsze znalezione wystąpienie, ponieważ iteracja przebiega od największej liczby."
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



