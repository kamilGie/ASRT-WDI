# ====================================================================================================>
# Zadanie 164
# Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę
# iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można
# założyć, że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna
# wpisać podzielniki do tablicyp pomocniczej. Przykład:60→[2,3,5]→2+3+5+2∗3+2∗5+3∗5+2∗3∗5=71
# ====================================================================================================>
# zadanie_164(60) -> print([2,3,5], 71)


def Zadanie_164(num):
    def divisiors(num):
        div = []
        i = 2

        while num > 1:
            if num % i == 0:
                div.append(i)

                while num % i == 0:
                    num //= i
            i += 1

        print(div, end=" ")
        return div

    def rek(t, curr_i=0, il=1):
        if curr_i == len(t):
            if il == 1:
                return
            nonlocal s
            s += il
            return

        rek(t, curr_i + 1, il)
        rek(t, curr_i + 1, il * t[curr_i])

    s = 0

    rek(divisiors(num))

    print(s)


