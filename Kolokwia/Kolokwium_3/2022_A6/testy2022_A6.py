import unittest
from contextlib import redirect_stdout
import io

from szablon2022_A6 import insert
from szablon2022_A6 import Node

class testy(unittest.TestCase):

    def test_Nr01_insert(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert((lambda n: (setattr(n, 'next', Node(31, Node(17, Node(703, Node(37, Node(707, Node(72, Node(29, Node(902 ,n))))))))), n)[1])(Node(2023)),303)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertIn(
                wynik, 
                {'2', '5'}, 
                msg=f"""dla zmiennych: (lambda n: (setattr(n, 'next', Node(31, Node(17, Node(703, Node(37, Node(707, Node(72, Node(29, Node(902 ,n))))))))), n)[1])(Node(2023)),303. Otrzymano: {wynik}, oczekiwano jedną z: {'2', '5'} """
            )

    def test_Nr02_insert(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert( (lambda n: (setattr(n, 'next', Node(23, Node(34, Node(45, Node(55, Node(515, Node( 51 ,n))))))), n)[1])(Node(12)),5125)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"""dla zmiennych:  (lambda n: (setattr(n, 'next', Node(23, Node(34, Node(45, Node(55, Node(515, Node( 51 ,n))))))), n)[1])(Node(12)),5125. Otrzymano: {wynik}, oczekiwano: '1' """)

    def test_Nr03_insert(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert( (lambda n: (setattr(n, 'next', Node(212, Node(23, Node(34, Node(45, Node(55, Node(515, Node( 51 ,n)))))))), n)[1])(Node(12)),2112)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"""dla zmiennych:  (lambda n: (setattr(n, 'next', Node(212, Node(23, Node(34, Node(45, Node(55, Node(515, Node( 51 ,n)))))))), n)[1])(Node(12)),2112. Otrzymano: {wynik}, oczekiwano: '0' """)

    def test_Nr04_insert(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert((lambda n: (setattr(n, 'next', Node(12, Node(23, Node(34, Node(45, Node( 56 ,n)))))), n)[1])(Node(101)),601)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"""dla zmiennych: (lambda n: (setattr(n, 'next', Node(12, Node(23, Node(34, Node(45, Node( 56 ,n)))))), n)[1])(Node(101)),601. Otrzymano: {wynik}, oczekiwano: '0' """)

    def test_Nr05_insert(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert((lambda n: (setattr(n, 'next', Node(12115, Node(12, Node(23, Node(34, Node(45, Node( 56 ,n))))))), n)[1])(Node(101)),601)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1', msg=f"""dla zmiennych: (lambda n: (setattr(n, 'next', Node(12115, Node(12, Node(23, Node(34, Node(45, Node( 56 ,n))))))), n)[1])(Node(101)),601. Otrzymano: {wynik}, oczekiwano: '1' """)

    def test_Nr06_insert(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert((lambda n: (setattr(n, 'next', Node(11, Node(111, Node( 1111 ,n)))), n)[1])(Node(1)),110)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0', msg=f"""dla zmiennych: (lambda n: (setattr(n, 'next', Node(11, Node(111, Node( 1111 ,n)))), n)[1])(Node(1)),110. Otrzymano: {wynik}, oczekiwano: '0' """)

    def test_Nr07_insert(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert(Node(101, Node(12, Node(123, Node(234, Node(345, Node(45, Node(56))))))),1234)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3', msg=f"""dla zmiennych: Node(101, Node(12, Node(123, Node(234, Node(345, Node(45, Node(56))))))),1234. Otrzymano: {wynik}, oczekiwano: '3' """)

    def test_Nr08_insert(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = insert(Node(101, Node(14, Node(41, Node(123, Node(234, Node(345, Node(45, Node(56)))))))),1234)
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '4', msg=f"""dla zmiennych: Node(101, Node(14, Node(41, Node(123, Node(234, Node(345, Node(45, Node(56)))))))),1234. Otrzymano: {wynik}, oczekiwano: '4' """)


def podpowiedz(nr: int):
    podpowiedzi = [
        "O ile została skrócona lista: Jeśli usuniemy 2 elementy i wstawimy 1 nowy, lista zostanie skrócona o 1 element.",
        "Na początku szukamy węzła, którego ostatnia cyfra jest taka sama jak pierwsza cyfra liczby `n`. Od tego węzła szukamy kolejnego węzła, którego pierwsza cyfra jest taka sama jak ostatnia cyfra `n`.",
        "Dopóki nie przejdziemy całej listy (pełnego cyklu), szukamy początkowego węzła. Gdy znajdziemy taki węzeł, rozpoczynamy nową pętlę w celu znalezienia końcowego węzła. Jeśli między tymi węzłami znajduje się więcej niż 2 elementy, łączymy te węzły za pomocą nowego węzła z wartością `n` i zwracamy długość skróconego odcinka. Jeśli nie znajdziemy odpowiedniego końca, przechodzimy do kolejnego możliwego początku."
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


