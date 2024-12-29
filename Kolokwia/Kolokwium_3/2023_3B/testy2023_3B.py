import unittest
from contextlib import redirect_stdout
import io

from szablon2023_3B import make_order
from szablon2023_3B import Node

class testy(unittest.TestCase):

    def test_Nr01_make_order(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = make_order(Node("ala", Node("ola", Node("abel", Node("ula", Node("irys", Node("ewa", Node("sroka", Node("gips")))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'gips -> abel ->  -> ewa -> irys -> ala ->  -> sroka -> ula -> ola', msg=f'''dla zmiennych: Node("ala", Node("ola", Node("abel", Node("ula", Node("irys", Node("ewa", Node("sroka", Node("gips")))))))). Otrzymano: {wynik}, oczekiwano: 'gips -> abel ->  -> ewa -> irys -> ala ->  -> sroka -> ula -> ola' ''')

    def test_Nr02_make_order(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = make_order(Node("abc", Node("def", Node("ghi"))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'ghi -> def -> abc ->  ->', msg=f'''dla zmiennych: Node("abc", Node("def", Node("ghi"))). Otrzymano: {wynik}, oczekiwano: 'ghi -> def -> abc ->  ->' ''')

    def test_Nr03_make_order(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = make_order(Node("zyx", Node("wvu", Node("tsr"))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '->  -> tsr -> wvu -> zyx', msg=f'''dla zmiennych: Node("zyx", Node("wvu", Node("tsr"))). Otrzymano: {wynik}, oczekiwano: '->  -> tsr -> wvu -> zyx' ''')

    def test_Nr04_make_order(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = make_order(Node("bac", Node("cab", Node("dac"))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '-> dac -> cab -> bac ->', msg=f'''dla zmiennych: Node("bac", Node("cab", Node("dac"))). Otrzymano: {wynik}, oczekiwano: '-> dac -> cab -> bac ->' ''')

    def test_Nr05_make_order(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = make_order(Node("ab", Node("ba", Node("abc", Node("cba", Node("bca", Node("xd", Node("dcba"))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'abc -> ab ->  -> bca ->  -> dcba -> xd -> cba -> ba', msg=f'''dla zmiennych: Node("ab", Node("ba", Node("abc", Node("cba", Node("bca", Node("xd", Node("dcba"))))))). Otrzymano: {wynik}, oczekiwano: 'abc -> ab ->  -> bca ->  -> dcba -> xd -> cba -> ba' ''')

    def test_Nr06_make_order(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = make_order(Node("abc", Node("cba", Node("bca", Node("cab", Node("acb", Node("bac")))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'abc ->  -> bac -> acb -> cab -> bca ->  -> cba', msg=f'''dla zmiennych: Node("abc", Node("cba", Node("bca", Node("cab", Node("acb", Node("bac")))))). Otrzymano: {wynik}, oczekiwano: 'abc ->  -> bac -> acb -> cab -> bca ->  -> cba' ''')

    def test_Nr07_make_order(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = make_order(Node("apple", Node("sroka", Node("orange", Node("xyz", Node("banana", Node("cde", Node("oro", Node("aaa")))))))))
                if wynik is not None: print(wynik)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, 'cde -> xyz ->  -> aaa -> oro -> banana -> orange -> apple ->  -> sroka', msg=f'''dla zmiennych: Node("apple", Node("sroka", Node("orange", Node("xyz", Node("banana", Node("cde", Node("oro", Node("aaa")))))))). Otrzymano: {wynik}, oczekiwano: 'cde -> xyz ->  -> aaa -> oro -> banana -> orange -> apple ->  -> sroka' ''')

def podpowiedz(nr: int):
    podpowiedzi = [
        "Stwórz 3 puste węzły pełniące rolę separatorów i przepinaj do nich węzły z głównego węzła.",
        "Stwórz funkcję, która sprawdza napisy i zwraca: 0, gdy litery w napisie są w porządku rosnącym, 1, gdy litery w napisie są w porządku malejącym, 2, gdy napis nie spełnia żadnego z powyższych warunków. W zależności od wyniku tej funkcji dopinaj węzły do wcześniej stworzonych separatorów",
        "Funkcja porównująca najpierw sprawdza pierwsze dwie litery, by ustalić początkowy porządek: rosnący lub malejący. Następnie iteracyjnie weryfikuje, czy reszta napisu zachowuje ten wzorzec. Jeśli nie,zwraca 2, oznaczając brak porządku"
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
