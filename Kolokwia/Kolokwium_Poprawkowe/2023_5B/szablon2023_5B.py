# ====================================================================================================>
# Zadanie 5B, 2024-02-06
# Dana jest tablica krotek 𝐿 = [(𝑥1, 𝑥2, 𝑦1, 𝑦2), …] gdzie 𝑥1, 𝑥2, 𝑦1, 𝑦2 oznaczają proste ograniczające
# kwadrat (𝑥1 < 𝑥2, 𝑦1 < 𝑦2). Proszę napisać funkcję thirteen(T), która zwraca wartość logiczną
# True, jeśli w danej tablicy można znaleźć 13 nienachodzących na siebie kwadratów, których suma pól
# jest równa 2024 i False w przeciwnym przypadku.
# ====================================================================================================>


def thirteen(T): ...


if __name__ == "__main__":
    from testy2023_5B import odpal_testy, podpowiedz

    thirteen( [ (0, 12, 0, 12), (12, 24, 0, 12), (24, 36, 0, 12), (36, 48, 0, 12), (48, 60, 0, 12), (60, 72, 0, 12), (72, 84, 0, 12), (84, 96, 0, 12), (96, 108, 0, 12), (108, 120, 0, 12), (0, 24, 13, 37), (0, 2, 38, 40), (2, 4, 38, 40), ])  # return True

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
