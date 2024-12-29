import unittest
from contextlib import redirect_stdout
import io

from szablon2021_6 import repair
from szablon2021_6 import Node


class testy(unittest.TestCase):

    def test_Nr01_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(4, Node(-32, Node(-128, Node(-2048)))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "6",
            msg=f"""dla zmiennych: Node(4, Node(-32, Node(-128, Node(-2048)))). Otrzymano: {wynik}, oczekiwano: '6' """,
        )

    def test_Nr02_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(1, Node(2, Node(8, Node(32)))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "2",
            msg=f"""dla zmiennych: Node(1, Node(2, Node(8, Node(32)))). Otrzymano: {wynik}, oczekiwano: '2' """,
        )

    def test_Nr03_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(64, Node(16, Node(4, Node(2)))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "2",
            msg=f"""dla zmiennych: Node(64, Node(16, Node(4, Node(2)))). Otrzymano: {wynik}, oczekiwano: '2' """,
        )

    def test_Nr04_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(64, Node(16, Node(4, Node(-2)))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "2",
            msg=f"""dla zmiennych: Node(64, Node(16, Node(4, Node(-2)))). Otrzymano: {wynik}, oczekiwano: '2' """,
        )

    def test_Nr05_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(16, Node(4, Node(1, Node(-0.5)))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "2",
            msg=f"""dla zmiennych: Node(16, Node(4, Node(1, Node(-0.5)))). Otrzymano: {wynik}, oczekiwano: '2' """,
        )

    def test_Nr06_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(1, Node(100, Node(1000, Node(10000, Node(100000))))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "1",
            msg=f"""dla zmiennych: Node(1, Node(100, Node(1000, Node(10000, Node(100000))))). Otrzymano: {wynik}, oczekiwano: '1' """,
        )

    def test_Nr07_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(2, Node(6.75, Node(10.125, Node(15.1875)))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "2",
            msg=f"""dla zmiennych: Node(2, Node(6.75, Node(10.125, Node(15.1875)))). Otrzymano: {wynik}, oczekiwano: '2' """,
        )

    def test_Nr08_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(256, Node(4, Node(1, Node(0.25)))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "2",
            msg=f"""dla zmiennych: Node(256, Node(4, Node(1, Node(0.25)))). Otrzymano: {wynik}, oczekiwano: '2' """,
        )

    def test_Nr09_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(1, Node(-64, Node(256, Node(-1024)))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "522",
            msg=f"""dla zmiennych: Node(1, Node(-64, Node(256, Node(-1024)))). Otrzymano: {wynik}, oczekiwano: '522' """,
        )

    def test_Nr10_repair(self):
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = repair(Node(16, Node(9, Node(-6.75, Node(5.0625)))))
            if wynik is not None:
                print(wynik)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "1",
            msg=f"""dla zmiennych: Node(16, Node(9, Node(-6.75, Node(5.0625)))). Otrzymano: {wynik}, oczekiwano: '1' """,
        )


def podpowiedz(nr: int):
    podpowiedzi = [
        "Na podstawie ilorazu dwóch pierwszych elementów należy znaleźć docelowy krok iloczynu.",
        "Docelowy krok iloczynu będzie ilorazem dwóch pierwszych elementów, spierwiastkowanym do odpowiedniej potęgi, zależnie od liczby kroków między pierwszym a drugim elementem. Na przykład, w ciągu 1 -> 16 -> 32, iloraz wynosi 16 i jest to jeden krok. Widzimy, że mnożąc 16 razy 16, nie otrzymamy 32, więc musimy dodać dodatkowy krok między 1 a 16. Pierwiastkujemy 16 do 2. potęgi i otrzymujemy 4. Dalej widzimy, że mnożąc 16 razy 4, nadal nie uzyskamy 32. Pierwiastkujemy więc 16 do 3. potęgi i otrzymujemy 2. Tym razem, mnożąc 16 razy 2, otrzymujemy 32, co oznacza, że jest to poprawny krok.",
        "Krok jest niepoprawny, jeśli mnożąc krok przez wartość poprzedniego węzła, przekroczymy wartość następnego węzła (wartość absolutna). Przejście nastąpi tylko wtedy, gdy krok jest większy od 1 lub mniejszy od -1. Jeśli krok mieści się w przedziale od -1 do 1, przejście nastąpi tylko wtedy, gdy wartość poprzedniego węzła  jest większa od wartości następnego węzła.",
    ]
    print(podpowiedzi[nr - 1])


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


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
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )
