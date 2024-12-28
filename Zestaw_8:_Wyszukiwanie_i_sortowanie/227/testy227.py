import unittest
from contextlib import redirect_stdout
import io

from szablon227 import insert_to_sorted, sort_by_insertion_sort
from szablon227 import Node

class testy(unittest.TestCase):

    def test_Nr01_insert_to_sorted(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert_to_sorted(Node(1, Node(3, Node(5))),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 5', msg=f"dla zmiennych: Node(1, Node(3, Node(5))),2. Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 5'")

    def test_Nr02_insert_to_sorted(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert_to_sorted(Node(1, Node(3, Node(5))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 3 -> 5 -> 6', msg=f"dla zmiennych: Node(1, Node(3, Node(5))),6. Otrzymano: {wynik}, oczekiwano: '1 -> 3 -> 5 -> 6'")

    def test_Nr03_insert_to_sorted(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert_to_sorted(Node(2, Node(4, Node(6))),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 4 -> 6', msg=f"dla zmiennych: Node(2, Node(4, Node(6))),1. Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 4 -> 6'")

    def test_Nr04_insert_to_sorted(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert_to_sorted(Node(1, Node(5, Node(10, Node(123, Node(123123))))),124)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 5 -> 10 -> 123 -> 124 -> 123123', msg=f"dla zmiennych: Node(1, Node(5, Node(10, Node(123, Node(123123))))),124. Otrzymano: {wynik}, oczekiwano: '1 -> 5 -> 10 -> 123 -> 124 -> 123123'")

    def test_Nr01_sort_by_insertion_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = sort_by_insertion_sort(Node(1, Node(5, Node(3, Node(2, Node(6, Node(8)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 5 -> 6 -> 8', msg=f"dla zmiennych: Node(1, Node(5, Node(3, Node(2, Node(6, Node(8)))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 5 -> 6 -> 8'")

    def test_Nr02_sort_by_insertion_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = sort_by_insertion_sort(Node(4, Node(2, Node(5, Node(1, Node(3))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5', msg=f"dla zmiennych: Node(4, Node(2, Node(5, Node(1, Node(3))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5'")

    def test_Nr03_sort_by_insertion_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = sort_by_insertion_sort(Node(10, Node(9, Node(8, Node(7, Node(6, Node(5)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 -> 6 -> 7 -> 8 -> 9 -> 10', msg=f"dla zmiennych: Node(10, Node(9, Node(8, Node(7, Node(6, Node(5)))))). Otrzymano: {wynik}, oczekiwano: '5 -> 6 -> 7 -> 8 -> 9 -> 10'")

    def test_Nr04_sort_by_insertion_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = sort_by_insertion_sort(Node(3, Node(3, Node(2, Node(1, Node(2))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 2 -> 3 -> 3', msg=f"dla zmiennych: Node(3, Node(3, Node(2, Node(1, Node(2))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 2 -> 3 -> 3'")

    def test_Nr05_sort_by_insertion_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = sort_by_insertion_sort(Node(5, Node(10, Node(5, Node(10, Node(1))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 5 -> 5 -> 10 -> 10', msg=f"dla zmiennych: Node(5, Node(10, Node(5, Node(10, Node(1))))). Otrzymano: {wynik}, oczekiwano: '1 -> 5 -> 5 -> 10 -> 10'")

    def test_Nr06_sort_by_insertion_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = sort_by_insertion_sort(Node(7, Node(3, Node(9, Node(2, Node(8, Node(1, Node(6, Node(4)))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9', msg=f"dla zmiennych: Node(7, Node(3, Node(9, Node(2, Node(8, Node(1, Node(6, Node(4)))))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9'")

    def test_Nr07_sort_by_insertion_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = sort_by_insertion_sort(Node(7, Node(3, Node(9, Node(2, Node(8, Node(1, Node(6, Node(4)))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9', msg=f"dla zmiennych: Node(7, Node(3, Node(9, Node(2, Node(8, Node(1, Node(6, Node(4)))))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9'")

    def test_Nr08_sort_by_insertion_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = sort_by_insertion_sort(Node(21, Node(19, Node(25, Node(17, Node(23, Node(16, Node(22, Node(18, Node(24, Node(20)))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25', msg=f"dla zmiennych: Node(21, Node(19, Node(25, Node(17, Node(23, Node(16, Node(22, Node(18, Node(24, Node(20)))))))))). Otrzymano: {wynik}, oczekiwano: '16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25'")

    def test_Nr09_sort_by_insertion_sort(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = sort_by_insertion_sort(Node(99, Node(98, Node(97, Node(96, Node(95, Node(94, Node(93, Node(92, Node(91))))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '91 -> 92 -> 93 -> 94 -> 95 -> 96 -> 97 -> 98 -> 99', msg=f"dla zmiennych: Node(99, Node(98, Node(97, Node(96, Node(95, Node(94, Node(93, Node(92, Node(91))))))))). Otrzymano: {wynik}, oczekiwano: '91 -> 92 -> 93 -> 94 -> 95 -> 96 -> 97 -> 98 -> 99'")


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

