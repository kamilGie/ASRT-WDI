from prime import prime
import re
import io
from typing import Any, Tuple, Callable
from contextlib import redirect_stdout

from _utils_T import (
    IMPORTY,
    KOMENDA,
    NAGLOWEK,
    ODPAL_TESTY,
    dynamiczny_import_funkcji,
    RAMKA,
)

TREES = {
    "Tree1": "Node(10, Node(5, Node(2), Node(7)), Node(15, Node(12), Node(20)))",
    "Tree2": "Node(50, Node(30, Node(20), Node(40)), Node(70, Node(60), Node(80)))",
    "Tree3": "Node(25, Node(15, Node(10), Node(20)), Node(35, Node(30), Node(40)))",
    "Tree4": "Node(100, Node(50, Node(25), Node(75)), Node(150, Node(125), Node(175)))",
    "Tree5": "Node(1, right=Node(2, right=Node(3, right=Node(4, right=Node(5)))))",
    "Tree6": "Node(60, Node(30, Node(10, Node(5), Node(20)), Node(50)), Node(90, Node(70), Node(110)))",
    "Tree7": "Node(45, Node(20, Node(10), Node(30)), Node(70, Node(60), Node(80)))",
    "Tree8": "Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))",
    "Tree9": "Node(100, Node(50, Node(25, Node(10), Node(30)), Node(75, Node(60), Node(90))), Node(150))",
    "Tree10": "Node(500, Node(200, Node(100, Node(50), Node(150)), Node(300, Node(250), Node(350))), Node(800))",
    "Tree11": "Node(5, Node(3, Node(2), Node(4)), Node(8, Node(7), Node(10)))",
    "Tree12": "Node(20, Node(10, Node(5, None, Node(7)), Node(15)), Node(30, Node(25), Node(35)))",
    "Tree13": "Node(75, Node(50, Node(25, Node(10), Node(30)), Node(60)), Node(100, Node(90), Node(110)))",
    "Tree14": "Node(150, Node(100, Node(50), Node(125)), Node(200, Node(175), Node(250)))",
    "Tree15": "Node(3, Node(2, Node(1)), Node(6, Node(5), Node(8)))",
    "Tree16": "Node(40, Node(20, Node(10), Node(30)), Node(60, Node(50), Node(70)))",
    "Tree17": "Node(90, Node(70, Node(60), Node(80)), Node(110, Node(100), Node(120)))",
    "Tree18": "Node(35, Node(20, Node(10), Node(30)), Node(50, Node(40), Node(60)))",
    "Tree19": "Node(200, Node(150, Node(100, Node(50)), Node(175)), Node(250, Node(225), Node(275)))",
    "Tree20": "Node(15, Node(10, Node(5), Node(12)), Node(20, Node(18), Node(25)))",
    "Tree21": "Node(21, Node(13, Node(2), Node(19)), Node(44, Node(28), None))",
    "Tree22": "Node(8, Node(6, Node(3), Node(7)), Node(20, Node(15), Node(22)))",
    "Tree23": "Node(10, Node(5, Node(2), Node(9)), Node(12, None, Node(18, Node(13), Node(22))))",
    "Tree24": "Node(16, Node(16, Node(16, Node(16), Node(16)), Node(2)), Node(99))",
    "Tree25": "Node(3, Node(2), Node(4, Node(1), Node(5)))",
    "Tree26": "Node(100, Node(50, None, Node(75)), Node(120))",
    "Tree27": "Node(1, Node(2, Node(4), Node(5)), Node(3, left=Node(6)))",
    "Tree28": "Node(11, Node(5, Node(2, Node(1), Node(4)), Node(7)), Node(15, Node(13), Node(20)))",
    "Tree29": "Node(42, Node(21, Node(10), Node(32)), Node(50))",
    "Tree30": "Node(60, Node(30, Node(15), Node(45, Node(40), Node(55))), Node(90, Node(75), None))",
    "Tree31": "Node(9, Node(12, Node(7), Node(3)), Node(15, Node(20), Node(10)))",
    "Tree32": "Node(5, Node(9, Node(3, Node(7), Node(2)), Node(4)), Node(8))",
    "Tree33": "Node(11, Node(6, Node(14, Node(8), Node(3)), Node(9)), Node(13))",
    "Tree34": "Node(25, Node(30, Node(35), Node(20)), Node(15, Node(10, Node(5), Node(17)), Node(40)))",
    "Tree35": "Node(2, Node(4, Node(8, Node(1), Node(3)), Node(6)), Node(5))",
    "Tree36": "Node(14, Node(13, Node(11), Node(12, Node(10), Node(9))), Node(8, None, Node(7)))",
    "Tree37": "Node(50, Node(40, Node(60), Node(30)), Node(20, Node(70), Node(10)))",
    "Tree38": "Node(7, Node(3, Node(1), Node(8, Node(5), Node(2))), Node(4, Node(6), None))",
    "Tree39": "Node(100, Node(90, Node(85, Node(95), None), Node(80)), Node(70, Node(75), Node(65, None, Node(60))))",
    "Tree40": "Node(1, Node(2, Node(4, Node(7), Node(3)), Node(5)), Node(6, Node(8, Node(10), Node(9)), None))",
}


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + '->' if self.left else ''}{self.val}{'->' + str(self.right) if self.right else ''}"


class drzewo_t(prime):
    def __str__(self) -> str:
        """
        Generuje testy dla zadania, wywołując odpowiednie metody w celu utworzenia
        struktury testów i ich wyników."""
        print(f"\nPisanie testów dla zadania nr: {self.nr_zadania}\n{RAMKA}")

        self.res = IMPORTY
        self.res += "\n"
        self.res += dynamiczny_import_funkcji(self.nr_zadania, self.funkcje)
        self.res += f"from szablon{self.nr_zadania} import Node"
        self.res += "\n\n"
        self.res += NAGLOWEK
        self.res += "\n"

        for funkcja in self.funkcje:
            self.generuj_testy_dla_funkcji(funkcja)

        self.finalizuj_testy()
        self.res += ODPAL_TESTY
        self.res += "\n"
        self.res += KOMENDA
        self.res += "\n"
        return self.res

    def transform_tree_syntax(self, input_string: str) -> str:

        def replace_tree_name(match):
            tree_name = match.group(0)
            return TREES.get(tree_name, tree_name)

        pattern = r"\bTree\d+\b"
        return re.sub(pattern, replace_tree_name, input_string)

    def wynik_wykonania_funkcji(
        self, funkcja: Callable, parametry: str
    ) -> Tuple[Any, bool]:
        """
        Uruchamia podaną funkcję z przekazanymi parametrami i przechwycuje jej wynik.

        Args:
            funkcja (Callable): Funkcja do uruchomienia.
            parametry (Tuple): Argumenty przekazywane do funkcji.

        Returns:
            Any: Zwraca wynik funkcji
            bool: Flaga wskazująca, czy wynik został zwrócony przez funkcję (False),
                  czy był wyprintowany na standardowe wyjście (True).
        """

        f = io.StringIO()
        with redirect_stdout(f):
            wynik = funkcja(*eval(f"[{parametry}]"))
            if wynik is not None:
                print(wynik)

        return repr(f.getvalue().strip()), True

    def pobierz_parametry(self, test_index: int, param_count: int) -> str:
        """
        Pobiera parametry testowe od użytkownika.

        Args:
            test_index (int): Indeks aktualnego testu.
            param_count (int): Liczba argumentów, które mają być pobrane.

        Returns:
            Tuple: Krotka z parametrami podanymi przez użytkownika.
        """
        if param_count == 0:
            return ""

        koncowka_argumetnow = "" if 1 == param_count else "y"
        wyjscie = ", lub 'stop' by zakonczyc testy" if test_index > 3 else ""
        wejscie = input(
            f"\nTest nr {test_index}\nPodaj {param_count} argument{koncowka_argumetnow} testowe{wyjscie}: "
        )
        print(f"\033[F\033[K\033[F\033[K\033[F\033[K", end="")
        wejscie = self.transform_tree_syntax(wejscie)
        print(wejscie)

        return wejscie
