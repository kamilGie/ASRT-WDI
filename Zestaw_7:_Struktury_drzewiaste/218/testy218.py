import unittest
from contextlib import redirect_stdout
import io

from szablon218 import Zadanie_218_rek, Zadanie_218_iter
from szablon218 import Node

class testy(unittest.TestCase):

    def test_Nr01_Zadanie_218_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2->3->5->7->10->12->15->20', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3. Otrzymano: {wynik}, oczekiwano: '2->3->5->7->10->12->15->20'")

    def test_Nr02_Zadanie_218_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2->5->6->7->10->12->15->20', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),6. Otrzymano: {wynik}, oczekiwano: '2->5->6->7->10->12->15->20'")

    def test_Nr03_Zadanie_218_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),11)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2->5->7->10->11->12->15->20', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),11. Otrzymano: {wynik}, oczekiwano: '2->5->7->10->11->12->15->20'")

    def test_Nr04_Zadanie_218_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),19)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2->5->7->10->12->15->19->20', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),19. Otrzymano: {wynik}, oczekiwano: '2->5->7->10->12->15->19->20'")

    def test_Nr05_Zadanie_218_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1->2->3->4->5->6', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6. Otrzymano: {wynik}, oczekiwano: '1->2->3->4->5->6'")


    def test_Nr07_Zadanie_218_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_rek(Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),105)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->25->30->50->60->75->90->100->105->110', msg=f"dla zmiennych: Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),105. Otrzymano: {wynik}, oczekiwano: '10->25->30->50->60->75->90->100->105->110'")

    def test_Nr08_Zadanie_218_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_rek(Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),120)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->25->30->50->60->75->90->100->110->120', msg=f"dla zmiennych: Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),120. Otrzymano: {wynik}, oczekiwano: '10->25->30->50->60->75->90->100->110->120'")

    def test_Nr09_Zadanie_218_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_rek(Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),200)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->25->30->50->60->75->90->100->110->200', msg=f"dla zmiennych: Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),200. Otrzymano: {wynik}, oczekiwano: '10->25->30->50->60->75->90->100->110->200'")

    def test_Nr10_Zadanie_218_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_rek(Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),76)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->25->30->50->60->75->76->90->100->110', msg=f"dla zmiennych: Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),76. Otrzymano: {wynik}, oczekiwano: '10->25->30->50->60->75->76->90->100->110'")

    def test_Nr01_Zadanie_218_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2->3->5->7->10->12->15->20', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3. Otrzymano: {wynik}, oczekiwano: '2->3->5->7->10->12->15->20'")

    def test_Nr02_Zadanie_218_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2->5->6->7->10->12->15->20', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),6. Otrzymano: {wynik}, oczekiwano: '2->5->6->7->10->12->15->20'")

    def test_Nr03_Zadanie_218_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),11)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2->5->7->10->11->12->15->20', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),11. Otrzymano: {wynik}, oczekiwano: '2->5->7->10->11->12->15->20'")

    def test_Nr04_Zadanie_218_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),19)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2->5->7->10->12->15->19->20', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),19. Otrzymano: {wynik}, oczekiwano: '2->5->7->10->12->15->19->20'")

    def test_Nr05_Zadanie_218_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1->2->3->4->5->6', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6. Otrzymano: {wynik}, oczekiwano: '1->2->3->4->5->6'")

    def test_Nr06_Zadanie_218_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_iter(Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),105)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->25->30->50->60->75->90->100->105->110', msg=f"dla zmiennych: Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),105. Otrzymano: {wynik}, oczekiwano: '10->25->30->50->60->75->90->100->105->110'")

    def test_Nr07_Zadanie_218_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_iter(Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),120)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->25->30->50->60->75->90->100->110->120', msg=f"dla zmiennych: Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),120. Otrzymano: {wynik}, oczekiwano: '10->25->30->50->60->75->90->100->110->120'")

    def test_Nr08_Zadanie_218_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_iter(Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),200)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->25->30->50->60->75->90->100->110->200', msg=f"dla zmiennych: Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),200. Otrzymano: {wynik}, oczekiwano: '10->25->30->50->60->75->90->100->110->200'")

    def test_Nr09_Zadanie_218_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = Zadanie_218_iter(Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),76)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '10->25->30->50->60->75->76->90->100->110', msg=f"dla zmiennych: Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))),76. Otrzymano: {wynik}, oczekiwano: '10->25->30->50->60->75->76->90->100->110'")


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

