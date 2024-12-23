import unittest
from contextlib import redirect_stdout
import io

from szablon205 import Zadanie_205
from szablon205 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_205(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_205(Node(1, Node(2, Node(3, Node(-1, Node(-2, Node(-3)))))),Node(0),Node(0))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(1, Node(2, Node(3, Node(-1, Node(-2, Node(-3)))))),Node(0),Node(0). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr02_Zadanie_205(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_205(Node(2, Node(4, Node(6, Node(8, Node(10, Node(-1, Node(-3, Node(-5)))))))),Node(0),Node(0))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(2, Node(4, Node(6, Node(8, Node(10, Node(-1, Node(-3, Node(-5)))))))),Node(0),Node(0). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr03_Zadanie_205(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_205(Node(1),Node(0),Node(0))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1),Node(0),Node(0). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr04_Zadanie_205(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_205(Node(1, Node(-1, Node(2, Node(-2, Node(3, Node(-3, Node(4, Node(-4, Node(5, Node(-5)))))))))),Node(0),Node(0))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(1, Node(-1, Node(2, Node(-2, Node(3, Node(-3, Node(4, Node(-4, Node(5, Node(-5)))))))))),Node(0),Node(0). Otrzymano: {wynik}, oczekiwano: '5'")


    def test_Nr05_Zadanie_205_zwalnianie_pamieci(self):
        head = Node(1, Node(-1, Node(2, Node(-2, Node(3, Node(-3, Node(4, Node(-4, Node(5, Node(-5))))))))))
        q,r=Node(0),Node(0)
        Zadanie_205(head,q,r)
        self.assertTrue(not head or not head.next,msg="nie zwolniono pamieci dla head")

    def test_Nr06_Zadanie_205_zapelnianie_p_q(self):
        head = Node(1, Node(-1, Node(2, Node(-2, Node(3, Node(-3, Node(4, Node(-4, Node(5, Node(-5))))))))))
        q,r=Node(0),Node(0)
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_205(head,q,r)
            print(q)
            print(r)
        wynik = f.getvalue().strip()
        self.assertTrue(
        wynik == '2 -> 4\n-1 -> -3 -> -5' or wynik == '0 -> 2 -> 4\n0 -> -1 -> -3 -> -5',
        msg=f"nie wypelniono poprawnie p lub q"
    )


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

