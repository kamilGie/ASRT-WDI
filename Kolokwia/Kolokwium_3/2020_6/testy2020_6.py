import unittest
from contextlib import redirect_stdout
import io

from szablon2020_6 import iloczyn
from szablon2020_6 import Node

class testy(unittest.TestCase):

    def test_Nr01_iloczyn(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iloczyn(Node(1,  Node(3)), Node(1, Node(2)), Node(1, Node(2,Node(3))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"""dla zmiennych: Node(1,  Node(3)), Node(1, Node(2)), Node(1, Node(2,Node(3))). Otrzymano: {wynik}, oczekiwano: '1' """)

    def test_Nr02_iloczyn(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iloczyn(Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(1, Node(2, Node(3, Node(4, Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5', msg=f"""dla zmiennych: Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(1, Node(2, Node(3, Node(4, Node(5))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5' """)

    def test_Nr03_iloczyn(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iloczyn(Node(2, Node(4, Node(6, Node(8)))),Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(2, Node(3, Node(4, Node(5, Node(7))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2 -> 4', msg=f"""dla zmiennych: Node(2, Node(4, Node(6, Node(8)))),Node(1, Node(2, Node(3, Node(4, Node(5))))),Node(2, Node(3, Node(4, Node(5, Node(7))))). Otrzymano: {wynik}, oczekiwano: '2 -> 4' """)

    def test_Nr04_iloczyn(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iloczyn(Node(1, Node(2, Node(3))),Node(3, Node(4, Node(5))),Node(3, Node(6, Node(7))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"""dla zmiennych: Node(1, Node(2, Node(3))),Node(3, Node(4, Node(5))),Node(3, Node(6, Node(7))). Otrzymano: {wynik}, oczekiwano: '3' """)

    def test_Nr05_iloczyn(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = iloczyn(Node(3, Node(6, Node(7))),Node(3, Node(4, Node(5))),Node(1, Node(2, Node(3))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"""dla zmiennych: Node(3, Node(6, Node(7))),Node(3, Node(4, Node(5))),Node(1, Node(2, Node(3))). Otrzymano: {wynik}, oczekiwano: '3' """)

def podpowiedz(nr: int):
    podpowiedzi = [
        "Wypinamy najmniejszą wartość.",
        "Jeśli najmniejsze wartości są takie same w trzech listach, dodajemy je do węzła wynikowego.",
        "Sprawdzamy pierwszy element węzła. Jeśli nie jest taki sam we wszystkich trzech listach, sprawdzamy, który element jest najmniejszy, a następnie wypinamy z list ktore posiadaja ten najmniejszy element. Powtarzamy to, aż jakis węzęł sie nie skończy."
    ]
    print(podpowiedzi[nr - 1])
def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


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


