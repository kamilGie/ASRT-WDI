# ====================================================================================================>
# Zadanie 159
# Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A
# cyfr 1 oraz B cyfr 0, gdzie A,B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca
# ilośćwszystkichmożliwychdozbudowanialiczb,takichżepierwszacyfrawsystemiedwójkowym(najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010 ,10100 ,11000
# (2) (2) (2)
# ====================================================================================================>


def Zadanie_159(A, B): ...


if __name__ == "__main__":
    from testy159 import odpal_testy

    Zadanie_159(int(input('Podaj A: ')), int(input('Podaj B: ')))

    # odpal_testy()
