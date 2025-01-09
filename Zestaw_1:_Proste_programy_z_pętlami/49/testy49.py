import unittest
from contextlib import redirect_stdout
import io

from szablon49 import Zadanie_49


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_49(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_49()
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '9998888777777', msg=f"""dla zmiennych: . Otrzymano: {wynik}, oczekiwano: '9998888777777' """)

def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


def podpowiedz(nr: int):
    podpowiedzi = [
        "minimalna liczba cyfr to 12, bo 11 cyfr 9 to 99  # maksymalnie 101 cyfr, jeśli same '1'",
        "Należy budować liczbę rekursywnie i sprawdzać, czy spełnia wymagane warunki."
        "https://www.youtube.com/watch?v=pcKY4hjDrxk"
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



