<picture>
  <source srcset="../../srt/zbior_zadan/157.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_157.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_157.png" alt="zadanie 157">
</picture>

```python
from math import sqrt, inf


def oblicz_srodek_ciezkosci(podzbior):
    """suma kazdego x i suma kazdego y podzielona przez ich ilosci"""
    liczba_punktow = len(podzbior)
    suma_x = sum(p[0] for p in podzbior)
    suma_y = sum(p[1] for p in podzbior)
    return (suma_x / liczba_punktow, suma_y / liczba_punktow)


def oblicz_odleglosc(p1, p2):
    """odległość euklidesową między dwoma punktami."""
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def generuj_podzbiory(tablica):
    """
    Generuje wszystkie możliwe podzbiory rekurencyjnie, dodając podzbiory z pierwszym
    elementem i bez pierwszego elementu tablicy, aż do dotarcia do końca tablicy.
    """
    if tablica == []:
        return [[]]

    podzbiory = generuj_podzbiory(tablica[1:])
    podzbiory_z_elementem = [[tablica[0]] + podzbior for podzbior in podzbiory]
    return podzbiory + podzbiory_z_elementem


def Zadanie_157(tablica):
    """
    Dla każdego, poza pustym, podzbiorem generuje środki ciężkości.
    Wszystkie środki ciężkości są porównywane, a następnie wyszukiwana jest najmniejsza różnica.
    """
    podzbiory = generuj_podzbiory(tablica)
    # to ze pusty jest pierwszy wynika ze znajomosci generuj_podzbiory jest to glupie rozwiazanie ale dla optymalizacji to zostawie
    podzbiory_bez_pustego = podzbiory[1:]
    srodki_ciezkosci = [oblicz_srodek_ciezkosci(p) for p in podzbiory_bez_pustego]

    min_odleglosc = inf
    for i in range(len(srodki_ciezkosci)):
        for j in range(i + 1, len(srodki_ciezkosci)):
            odleglosc = oblicz_odleglosc(srodki_ciezkosci[i], srodki_ciezkosci[j])
            min_odleglosc = min(min_odleglosc, odleglosc)

    return min_odleglosc

```

---
Gwiazdka motywuje do rozwijania projektu 🙏
