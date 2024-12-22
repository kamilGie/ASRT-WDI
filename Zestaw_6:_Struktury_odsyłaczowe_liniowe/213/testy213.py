import unittest
from contextlib import redirect_stdout
import io

from szablon213 import repair
from szablon213 import Node

class testy(unittest.TestCase):

    def test_Nr01_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(4, Node(12, Node(20, Node(28, Node(36, Node(44, Node(60))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(4, Node(12, Node(20, Node(28, Node(36, Node(44, Node(60))))))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr02_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(5, Node(15, Node(25, Node(45, Node(55, Node(75)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(5, Node(15, Node(25, Node(45, Node(55, Node(75)))))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr03_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(10, Node(20, Node(30, Node(50, Node(70))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(10, Node(20, Node(30, Node(50, Node(70))))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr04_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(3, Node(6, Node(9, Node(15, Node(18))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(3, Node(6, Node(9, Node(15, Node(18))))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr05_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(100, Node(150, Node(200, Node(300)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(100, Node(150, Node(200, Node(300)))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr06_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(100, Node(80, Node(60, Node(20)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(100, Node(80, Node(60, Node(20)))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr07_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(50, Node(40, Node(30, Node(10)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(50, Node(40, Node(30, Node(10)))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr08_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(90, Node(75, Node(45))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(90, Node(75, Node(45))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr09_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(1000, Node(950, Node(850))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1000, Node(950, Node(850))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr10_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(1, Node(3, Node(7, Node(9, Node(15, Node(21, Node(27, Node(35)))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10', msg=f"dla zmiennych: Node(1, Node(3, Node(7, Node(9, Node(15, Node(21, Node(27, Node(35)))))))). Otrzymano: {wynik}, oczekiwano: '10'")

    def test_Nr11_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(50, Node(45, Node(40, Node(25, Node(20, Node(10)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(50, Node(45, Node(40, Node(25, Node(20, Node(10)))))). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr12_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(2, Node(4, Node(8, Node(16, Node(32))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '11', msg=f"dla zmiennych: Node(2, Node(4, Node(8, Node(16, Node(32))))). Otrzymano: {wynik}, oczekiwano: '11'")

    def test_Nr13_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(4, Node(12, Node(20, Node(32)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(4, Node(12, Node(20, Node(32)))). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr14_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(4, Node(12, Node(20, Node(32, Node(33))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '25', msg=f"dla zmiennych: Node(4, Node(12, Node(20, Node(32, Node(33))))). Otrzymano: {wynik}, oczekiwano: '25'")

    def test_Nr15_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(2, Node(8, Node(14, Node(20, Node(26, Node(30)))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '9', msg=f"dla zmiennych: Node(2, Node(8, Node(14, Node(20, Node(26, Node(30)))))). Otrzymano: {wynik}, oczekiwano: '9'")

    def test_Nr16_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(10, Node(16, Node(22, Node(34)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(10, Node(16, Node(22, Node(34)))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr17_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(50, Node(70, Node(90, Node(96)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '20', msg=f"dla zmiennych: Node(50, Node(70, Node(90, Node(96)))). Otrzymano: {wynik}, oczekiwano: '20'")

    def test_Nr18_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(3, Node(9, Node(27))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(3, Node(9, Node(27))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr19_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(100, Node(80, Node(60, Node(56)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '8', msg=f"dla zmiennych: Node(100, Node(80, Node(60, Node(56)))). Otrzymano: {wynik}, oczekiwano: '8'")

    def test_Nr20_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(1, Node(7, Node(13, Node(16)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(1, Node(7, Node(13, Node(16)))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr21_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(30, Node(20, Node(10, Node(5)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(30, Node(20, Node(10, Node(5)))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr22_repair(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = repair(Node(5, Node(1, Node(-3, Node(-11)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(5, Node(1, Node(-3, Node(-11)))). Otrzymano: {wynik}, oczekiwano: '1'")


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

