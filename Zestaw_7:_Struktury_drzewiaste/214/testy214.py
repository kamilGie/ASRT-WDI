import unittest
from contextlib import redirect_stdout
import io

from szablon214 import wypisz_rek, wypisz_iter, wypisz_iter_morris, czy_nalezy_rek, czy_nalezy_iter, rozmiar_rek, rozmiar_iter, wysokosc_rek, wysokosc_iter, liczba_lisci_rek, liczba_lisci_iter, wezly_na_poziomie_rek, wezly_na_poziomie_iter, wezly_z_jednym_potomkiem_rek, wezly_z_jednym_potomkiem_iter
from szablon214 import Node

class testy(unittest.TestCase):

    def test_Nr01_czy_nalezy_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),5. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr02_czy_nalezy_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),10)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),10. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr03_czy_nalezy_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3. Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr04_czy_nalezy_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr05_czy_nalezy_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),5. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr06_czy_nalezy_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6. Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr01_czy_nalezy_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),5. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr02_czy_nalezy_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),10)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),10. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr03_czy_nalezy_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3. Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr04_czy_nalezy_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr05_czy_nalezy_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),5)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'True', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),5. Otrzymano: {wynik}, oczekiwano: 'True'")

    def test_Nr06_czy_nalezy_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = czy_nalezy_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'False', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),6. Otrzymano: {wynik}, oczekiwano: 'False'")

    def test_Nr01_rozmiar_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = rozmiar_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '7', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '7'")

    def test_Nr02_rozmiar_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = rozmiar_rek(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '9', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)). Otrzymano: {wynik}, oczekiwano: '9'")

    def test_Nr03_rozmiar_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = rozmiar_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr04_rozmiar_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = rozmiar_rek(Node(10, Node(5, Node(2), Node(9)), Node(12, None, Node(18, Node(13), Node(22)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '8', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(9)), Node(12, None, Node(18, Node(13), Node(22)))). Otrzymano: {wynik}, oczekiwano: '8'")

    def test_Nr01_rozmiar_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = rozmiar_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '7', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '7'")

    def test_Nr02_rozmiar_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = rozmiar_iter(Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '9', msg=f"dla zmiennych: Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))). Otrzymano: {wynik}, oczekiwano: '9'")

    def test_Nr03_rozmiar_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = rozmiar_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr04_rozmiar_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = rozmiar_iter(Node(10, Node(5, Node(2), Node(9)), Node(12, None, Node(18, Node(13), Node(22)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '8', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(9)), Node(12, None, Node(18, Node(13), Node(22)))). Otrzymano: {wynik}, oczekiwano: '8'")

    def test_Nr05_rozmiar_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = rozmiar_iter(Node(3, Node(2), Node(4, Node(1), Node(5))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(3, Node(2), Node(4, Node(1), Node(5))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr01_wysokosc_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wysokosc_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr02_wysokosc_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wysokosc_rek(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr03_wysokosc_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wysokosc_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr04_wysokosc_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wysokosc_rek(Node(100, Node(50, None, Node(75)), Node(120)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(100, Node(50, None, Node(75)), Node(120)). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr01_wysokosc_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wysokosc_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr02_wysokosc_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wysokosc_iter(Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr03_wysokosc_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wysokosc_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr04_wysokosc_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wysokosc_iter(Node(100, Node(50, None, Node(75)), Node(120)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(100, Node(50, None, Node(75)), Node(120)). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr05_wysokosc_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wysokosc_iter(Node(50, Node(40, Node(60), Node(30)), Node(20, Node(70), Node(10))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"dla zmiennych: Node(50, Node(40, Node(60), Node(30)), Node(20, Node(70), Node(10))). Otrzymano: {wynik}, oczekiwano: '3'")

    def test_Nr01_liczba_lisci_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr02_liczba_lisci_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr03_liczba_lisci_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_rek(Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr04_liczba_lisci_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_rek(Node(100, Node(50, None, Node(75)), Node(120)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(100, Node(50, None, Node(75)), Node(120)). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr05_liczba_lisci_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_rek(Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr01_liczba_lisci_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr02_liczba_lisci_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr03_liczba_lisci_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_iter(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr04_liczba_lisci_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_iter(Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5', msg=f"dla zmiennych: Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))). Otrzymano: {wynik}, oczekiwano: '5'")

    def test_Nr05_liczba_lisci_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_iter(Node(16, Node(16, Node(16, Node(16), Node(16)), Node(2)), Node(99)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(16, Node(16, Node(16, Node(16), Node(16)), Node(2)), Node(99)). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr06_liczba_lisci_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_iter(Node(10, Node(5, Node(2), Node(9)), Node(12, None, Node(18, Node(13), Node(22)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(9)), Node(12, None, Node(18, Node(13), Node(22)))). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr07_liczba_lisci_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = liczba_lisci_iter(Node(100, Node(50, None, Node(75)), Node(120)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(100, Node(50, None, Node(75)), Node(120)). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr01_wezly_na_poziomie_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3. Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr02_wezly_na_poziomie_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2. Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr03_wezly_na_poziomie_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),1. Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr04_wezly_na_poziomie_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),0)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),0. Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr05_wezly_na_poziomie_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),4)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),4. Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr01_wezly_na_poziomie_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),4)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),4. Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr02_wezly_na_poziomie_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),3. Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr03_wezly_na_poziomie_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),2. Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr04_wezly_na_poziomie_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),1)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),1. Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr05_wezly_na_poziomie_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),0)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))),0. Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr06_wezly_na_poziomie_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),4)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),4. Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr07_wezly_na_poziomie_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_na_poziomie_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),0)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))),0. Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr01_wezly_z_jednym_potomkiem_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_rek(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr02_wezly_z_jednym_potomkiem_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_rek(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr03_wezly_z_jednym_potomkiem_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_rek(Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr04_wezly_z_jednym_potomkiem_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_rek(Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13)))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr05_wezly_z_jednym_potomkiem_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_rek(Node(21, Node(13, Node(2), Node(19)), Node(44, Node(28), None)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(21, Node(13, Node(2), Node(19)), Node(44, Node(28), None)). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr06_wezly_z_jednym_potomkiem_rek(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_rek(Node(60, Node(30, Node(15), Node(45, Node(40), Node(55))), Node(90, Node(75), None)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(60, Node(30, Node(15), Node(45, Node(40), Node(55))), Node(90, Node(75), None)). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr01_wezly_z_jednym_potomkiem_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_iter(Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20))). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr02_wezly_z_jednym_potomkiem_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_iter(Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"dla zmiennych: Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5))))). Otrzymano: {wynik}, oczekiwano: '4'")

    def test_Nr03_wezly_z_jednym_potomkiem_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_iter(Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110))). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr04_wezly_z_jednym_potomkiem_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_iter(Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150)). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr05_wezly_z_jednym_potomkiem_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_iter(Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13)))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '2', msg=f"dla zmiennych: Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13)))). Otrzymano: {wynik}, oczekiwano: '2'")

    def test_Nr06_wezly_z_jednym_potomkiem_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_iter(Node(11, Node(6, Node(14, Node(8), Node(3)), Node(9)), Node(13)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(11, Node(6, Node(14, Node(8), Node(3)), Node(9)), Node(13)). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr07_wezly_z_jednym_potomkiem_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_iter(Node(100, Node(50, None, Node(75)), Node(120)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(100, Node(50, None, Node(75)), Node(120)). Otrzymano: {wynik}, oczekiwano: '1'")

    def test_Nr08_wezly_z_jednym_potomkiem_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_iter(Node(42, Node(21, Node(10), Node(32)), Node(50)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"dla zmiennych: Node(42, Node(21, Node(10), Node(32)), Node(50)). Otrzymano: {wynik}, oczekiwano: '0'")

    def test_Nr09_wezly_z_jednym_potomkiem_iter(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = wezly_z_jednym_potomkiem_iter(Node(21, Node(13, Node(2), Node(19)), Node(44, Node(28), None)))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"dla zmiennych: Node(21, Node(13, Node(2), Node(19)), Node(44, Node(28), None)). Otrzymano: {wynik}, oczekiwano: '1'")


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

