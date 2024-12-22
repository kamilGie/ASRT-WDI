from input_main import input_main
from _utils_S import parsuj_prototyp, main
from inspect import signature


class Node:
    pass


def lista_przesylaczowa():
    return """

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")\n\n\n\n\n\n
"""


class przesylaczowe_s(input_main):
    def __str__(self) -> str:
        res = parsuj_prototyp(self.linie_prototypu, self.funkcje, lista_przesylaczowa())

        wywolania_funkcji = "\n"
        for funkcja in self.funkcje:
            sig = signature(funkcja)

            input_lines = []
            for (
                param_name
            ) in sig.parameters:  # Iterujesz po kluczach, które są nazwami parametrów
                if param_name in {"p", "q", "head"}:
                    input_lines.append(f"Node(1, Node(2, Node(3)))")
                else:
                    input_lines.append(f"int(input('Podaj {param_name}: '))")

            wywolania_funkcji += (
                f"\n    {funkcja.__name__}({', '.join(input_lines)})\n\n"
            )

        res += "\n\n\n\n"
        res += main(self.nr_zadania, wywolania_funkcji)

        return res
