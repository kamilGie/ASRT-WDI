# ====================================================================================================>
# Zadanie 5B, 2024-02-06
# Dana jest tablica krotek 𝐿 = [(𝑥1, 𝑥2, 𝑦1, 𝑦2), …] gdzie 𝑥1, 𝑥2, 𝑦1, 𝑦2 oznaczają proste ograniczające
# kwadrat (𝑥1 < 𝑥2, 𝑦1 < 𝑦2). Proszę napisać funkcję thirteen(T), która zwraca wartość logiczną
# True, jeśli w danej tablicy można znaleźć 13 nienachodzących na siebie kwadratów, których suma pól
# jest równa 2024 i False w przeciwnym przypadku.
# ====================================================================================================>

def pole(proste) -> int:
    return (proste[1] - proste[0]) ** 2


def nachodza(k1, k2) -> bool:
    """Nachodzenie zachodzi, jeśli kwadrat nie leży całkowicie po lewej, prawej, poniżej lub powyżej drugiego."""
    lewo = k1[1] <= k2[0]
    prawo = k1[0] >= k2[1]
    dol = k1[3] <= k2[2]
    gora = k1[2] >= k2[3]

    return not (lewo or prawo or dol or gora)


def thirteen(T):
    wymagana_liczba_kwadratow = 13
    wymagane_pole_kwadratow = 2024

    def rek(idx=0, szukane_pole=wymagane_pole_kwadratow, kwadraty=[]):

        # Zwracamy True, jeśli na liście znajduje się 13 kwadratów, a `szukane_pole` wynosi 0.
        if len(kwadraty) == wymagana_liczba_kwadratow and szukane_pole == 0:
            return True

        # Zwracamy False, jeśli doszliśmy do końca listy kwadratów, lista kwadratów jest za duża lub suma pól przekroczyła 0.
        if ( idx == len(T) or len(kwadraty) > wymagana_liczba_kwadratow or szukane_pole < 0):
            return False

        # Jeśli kwadrat nie nachodzi na żaden z kwadratów w tej liście, 
        if not any(nachodza(T[idx], kwadrat) for kwadrat in kwadraty):
            # sprawdzamy, czy funkcja, dodając go do listy oraz zmniejszając szukane pole o pole tego kwadratu zwroci true
            if rek(idx + 1, szukane_pole - pole(T[idx]), kwadraty + [T[idx]]):
                return True

        return rek(idx + 1, szukane_pole, kwadraty)

    return rek()


