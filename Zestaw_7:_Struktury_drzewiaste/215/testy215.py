import unittest
from contextlib import redirect_stdout
import io

from szablon215 import usun_wszystkie_wezly, usun_wezly_powyzej_poziomu, usun_liscie
from szablon215 import Node

class testy(unittest.TestCase):

    def test_Nr01_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5->10->15', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2. Otrzymano: {wynik}, oczekiwano: '5->10->15'")

    def test_Nr02_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),1. Otrzymano: {wynik}, oczekiwano: '10'")

    def test_Nr03_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '25->50->75->100->150', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)),3. Otrzymano: {wynik}, oczekiwano: '25->50->75->100->150'")

    def test_Nr04_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '50->100->150', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)),2. Otrzymano: {wynik}, oczekiwano: '50->100->150'")

    def test_Nr05_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '100', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)),1. Otrzymano: {wynik}, oczekiwano: '100'")

    def test_Nr06_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->25->30->50->60->75->90->100->150', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)),5. Otrzymano: {wynik}, oczekiwano: '10->25->30->50->60->75->90->100->150'")

    def test_Nr07_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),4)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1->2->3->4', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),4. Otrzymano: {wynik}, oczekiwano: '1->2->3->4'")

    def test_Nr08_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1->2->3', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),3. Otrzymano: {wynik}, oczekiwano: '1->2->3'")

    def test_Nr09_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1->2', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),2. Otrzymano: {wynik}, oczekiwano: '1->2'")

    def test_Nr10_usun_wezly_powyzej_poziomu(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_wezly_powyzej_poziomu(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),1. Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr01_usun_liscie(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_liscie(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5->10->15', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '5->10->15'")

    def test_Nr02_usun_liscie(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_liscie(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1->2->3->4', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '1->2->3->4'")

    def test_Nr03_usun_liscie(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_liscie(Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->30->60->90', msg=f"dla zmiennych: Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))). Otrzymano: {wynik}, oczekiwano: '10->30->60->90'")

    def test_Nr04_usun_liscie(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_liscie(Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3->6->8->10->14', msg=f"dla zmiennych: Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13)))). Otrzymano: {wynik}, oczekiwano: '3->6->8->10->14'")

    def test_Nr05_usun_liscie(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_liscie(Node(90, Node(70, Node(60), Node(80)), Node(110, Node(100), Node(120))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '70->90->110', msg=f"dla zmiennych: Node(90, Node(70, Node(60), Node(80)), Node(110, Node(100), Node(120))). Otrzymano: {wynik}, oczekiwano: '70->90->110'")

    def test_Nr06_usun_liscie(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = usun_liscie(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '25->50->75->100', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)). Otrzymano: {wynik}, oczekiwano: '25->50->75->100'")


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

