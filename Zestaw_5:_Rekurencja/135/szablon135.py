# ====================================================================================================>
# Zadanie 135
# Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
# zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i
# kolumnie k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy
# minimalny koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt
# przebywania na polu startowym i ostatnim także wliczamy do kosztu przejścia.
# ====================================================================================================>


def Zadanie_135(t, k): ...


if __name__ == "__main__":
    from testy135 import odpal_testy

    Zadanie_135(int(input('Podaj t: ')), int(input('Podaj k: ')))

    # odpal_testy()
