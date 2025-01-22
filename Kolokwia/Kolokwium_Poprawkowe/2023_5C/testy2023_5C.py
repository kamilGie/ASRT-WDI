import unittest
from contextlib import redirect_stdout
import io

from szablon2023_5C import divide
from szablon2023_5C import Node

class testy(unittest.TestCase):

    def test_Nr01_divide(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wynik = divide(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13, Node(14, Node(15, Node(16, Node(17, Node(18, Node(19, Node(20, Node(21, Node(22, Node(23, Node(24, Node(25, Node(26, Node(27, Node(28, Node(29, Node(30, Node(31, Node(32, Node(33, Node(34, Node(35, Node(36, Node(37, Node(38, Node(39, Node(40, Node(41, Node(42, Node(43, Node(44, Node(45, Node(46, Node(47, Node(48, Node(49, Node(50, Node(51, Node(52, Node(53, Node(54, Node(55, Node(56, Node(57, Node(58, Node(59, Node(60, Node(61, Node(62, Node(63, Node(64, Node(65, Node(66, Node(67, Node(68, Node(69, Node(70, Node(71, Node(72, Node(73, Node(74, Node(75, Node(76, Node(77, Node(78, Node(79, Node(80, Node(81, Node(82, Node(83, Node(84, Node(85, Node(86, Node(87, Node(88, Node(89, Node(90, Node(91, Node(92, Node(93, Node(94, Node(95, Node(96, Node(97, Node(98, Node(99, Node(100)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
                print(wynik[0])
                print(wynik[1])

            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 9 -> 10 -> 11 -> 13 -> 14 -> 15 -> 17 -> 19 -> 21 -> 22 -> 23 -> 25 -> 26 -> 29 -> 30 -> 31 -> 33 -> 34 -> 35 -> 37 -> 38 -> 39 -> 41 -> 42 -> 43 -> 46 -> 47 -> 49 -> 51 -> 53 -> 55 -> 57 -> 58 -> 59 -> 61 -> 62 -> 65 -> 66 -> 67 -> 69 -> 70 -> 71 -> 73 -> 74 -> 77 -> 78 -> 79 -> 82 -> 83 -> 85 -> 86 -> 87 -> 89 -> 91 -> 93 -> 94 -> 95 -> 97\n8 -> 12 -> 16 -> 18 -> 20 -> 24 -> 27 -> 28 -> 32 -> 36 -> 40 -> 44 -> 45 -> 48 -> 50 -> 52 -> 54 -> 56 -> 60 -> 63 -> 64 -> 68 -> 72 -> 75 -> 76 -> 80 -> 81 -> 84 -> 88 -> 90 -> 92 -> 96 -> 98 -> 99 -> 100', msg=f"""dla zmiennych: Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13, Node(14, Node(15, Node(16, Node(17, Node(18, Node(19, Node(20, Node(21, Node(22, Node(23, Node(24, Node(25, Node(26, Node(27, Node(28, Node(29, Node(30, Node(31, Node(32, Node(33, Node(34, Node(35, Node(36, Node(37, Node(38, Node(39, Node(40, Node(41, Node(42, Node(43, Node(44, Node(45, Node(46, Node(47, Node(48, Node(49, Node(50, Node(51, Node(52, Node(53, Node(54, Node(55, Node(56, Node(57, Node(58, Node(59, Node(60, Node(61, Node(62, Node(63, Node(64, Node(65, Node(66, Node(67, Node(68, Node(69, Node(70, Node(71, Node(72, Node(73, Node(74, Node(75, Node(76, Node(77, Node(78, Node(79, Node(80, Node(81, Node(82, Node(83, Node(84, Node(85, Node(86, Node(87, Node(88, Node(89, Node(90, Node(91, Node(92, Node(93, Node(94, Node(95, Node(96, Node(97, Node(98, Node(99, Node(100)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))). Otrzymano: {wynik}, oczekiwano: '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 9 -> 10 -> 11 -> 13 -> 14 -> 15 -> 17 -> 19 -> 21 -> 22 -> 23 -> 25 -> 26 -> 29 -> 30 -> 31 -> 33 -> 34 -> 35 -> 37 -> 38 -> 39 -> 41 -> 42 -> 43 -> 46 -> 47 -> 49 -> 51 -> 53 -> 55 -> 57 -> 58 -> 59 -> 61 -> 62 -> 65 -> 66 -> 67 -> 69 -> 70 -> 71 -> 73 -> 74 -> 77 -> 78 -> 79 -> 82 -> 83 -> 85 -> 86 -> 87 -> 89 -> 91 -> 93 -> 94 -> 95 -> 97\n8 -> 12 -> 16 -> 18 -> 20 -> 24 -> 27 -> 28 -> 32 -> 36 -> 40 -> 44 -> 45 -> 48 -> 50 -> 52 -> 54 -> 56 -> 60 -> 63 -> 64 -> 68 -> 72 -> 75 -> 76 -> 80 -> 81 -> 84 -> 88 -> 90 -> 92 -> 96 -> 98 -> 99 -> 100' """)

def podpowiedz(nr: int):
    podpowiedzi = [
    "Tworzymy listę, odczepiając elementy od początkowej.",
    "Odczepiamy, gdy w rozkładzie na czynniki pierwsze mamy dwa razy tę samą liczbę pierwszą i coś innego.",
    "Iterujemy od 2 i sprawdzamy, czy liczba jest pierwsza. Jeśli tak, sprawdzamy, czy można podzielić naszą liczbę przez kwadrat tej liczby. Jeśli się da, sprawdzamy, czy po podzieleniu naszej liczby przez ten kwadrat wynik jest większy niż 2.",
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


