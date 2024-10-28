# ====================================================================================================>
# Zadanie 10
# Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.
# ====================================================================================================>


def Zadanie_10(liczba):
    if liczba < 2:
        return False
    else:
        dzielnik = 2
        while dzielnik**2 <= liczba:
            if liczba % dzielnik == 0:
                return False
            dzielnik += 1
        return True
