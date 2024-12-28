def podpowiedz():
    return """    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)\n"""


def przykladowe_odpalenie(funkcja):
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

    """
    Przygotowuje dynamiczne wywołanie funkcji i zwraca przykład wraz z wynikiem w formacie:
    funkcja(parametry z input) # return wynik
    """
    print()
    while True:
        try:
            parametry_uzytkonwika = input(
                "Podaj argumenty przykładowego wywołania, które pojawi się w szablonie: "
            )
            param_values = eval(parametry_uzytkonwika)
            if not isinstance(param_values, tuple):
                param_values = (param_values,)

            result = funkcja(*param_values)
        except Exception as e:
            print(f"Błąd: {e}. Spróbuj ponownie.")
            continue
        example_with_result = (
            f"    {funkcja.__name__}({parametry_uzytkonwika})  # return {result}"
        )
        print(f"\nPrzykład z wynikiem: {example_with_result}")
        break

    return example_with_result


def parsuj_prototyp(linie_prototypu, funkcje, naglokowa_funkcja=""):
    """
    Pobiera wszystkie komentarze początkowe, a następnie dodaje nagłówki funkcji
    (z zadanych funkcji w `funkcje`) i zamienia ich ciało na '...'.
    Kończy przetwarzanie po napotkaniu `if __name__ == "__main__"`.
    """
    res = ""
    wstep = True
    for linia in linie_prototypu:
        if wstep:
            if linia.strip().startswith("#"):
                res += linia
            else:
                wstep = False
                res += naglokowa_funkcja
        elif any(linia.startswith(f"def {f.__name__}") for f in funkcje):
            res += "\n\n" + linia.replace("\n", "") + " ...\n\n"
        elif 'if __name__ == "__main__":\n' in linia:
            return res
    return res


def main(nr_zadania, cialo_maina="\n\n"):
    """
    Generuje blok `main`. Pozwala na dodanie niestandardowego
    kodu `cialo_maina`, jeśli środek bloku `main` wymaga specyficznych operacji.
    """
    res = '\nif __name__ == "__main__":\n'
    res += f"    from testy{nr_zadania} import odpal_testy, podpowiedz\n"
    res += cialo_maina
    res += f"\n    # odpal_testy()\n"
    return res
