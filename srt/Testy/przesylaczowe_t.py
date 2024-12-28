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
    stworz_podpowiedzi,
)


class Node:
    """lista dwukierunkowa, w zadaniach gdzie jest jednokierunkowa 2 kierunek"""

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next: Node | None = next
        self.prev: Node | None = prev
        if next:
            next.prev = self
        if prev:
            prev.next = self

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


class przesylaczowe_t(prime):
    def __str__(self) -> str:
        """
        Generuje testy dla zadania, wywołując odpowiednie metody w celu utworzenia
        struktury testów i ich wyników.
        """
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

        self.res += stworz_podpowiedzi()
        self.res += "\n"
        self.res += ODPAL_TESTY
        self.res += "\n"
        self.res += KOMENDA
        self.res += "\n"
        self.finalizuj_testy()
        return self.res

    def transform_node_syntax(self, input_string):
        """
        Główna metoda, wyszukuje wzorce Node(...)
        i podmienia składnię z '>' i 'cX'
        na kod z lambdami zapewniającymi cykliczność.
        """

        def _make_linear_chain(arr):
            """rekurecyjnie tworzy Node"""
            if len(arr) == 0:
                return ""
            if len(arr) == 1:
                return f"Node({arr[0]})"
            head, *rest = arr
            return f"Node({head}, {_make_linear_chain(rest)})"

        def _replace_node(match):
            content = match.group(1)
            tokens = content.split(">")
            c_index = None
            c_label = None
            cleaned = []

            # Szukamy czy cykliczny
            for i, token in enumerate(tokens):
                token = token.strip()
                if token.startswith("c"):
                    c_index = i
                    c_label = token[1:]  # np. "c3" -> "3"
                else:
                    cleaned.append(token)

            # Jeśli nie ma cyklicznego tokenu:
            if c_index is None:
                return _make_linear_chain(cleaned)

            # tworze cykliczna czesci
            after_c = tokens[c_index + 1 :]
            # dopisuje do ostatniego elementu wskazanie na element n
            after_c[-1] = f" { after_c[-1] } ,n"
            tail_str = _make_linear_chain(after_c)
            lambda_part = (
                f"(lambda n: (setattr(n, 'next', {tail_str}), n)[1])(Node({c_label}))"
            )

            before_c = tokens[:c_index]
            if not before_c:  # sam cykl
                return lambda_part

            res_node = before_c
            # dopisuje do ostatniego elementu przed cyklem zeby wskazywal na lambde ktora stworzylem
            res_node[-1] = f"{ res_node[-1] },{ lambda_part }"
            return _make_linear_chain(res_node)

        pattern = r"Node\(([^()]+)\)"
        return re.sub(pattern, _replace_node, input_string)

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
        wejscie = self.transform_node_syntax(wejscie)
        print(wejscie)

        return wejscie
