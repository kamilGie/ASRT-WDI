<picture>
  <source srcset="../../srt/zbior_zadan/097.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_097.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_097.png" alt="zadanie 097">
</picture>

```python
from math import inf


def Zadanie_97(T1):
    """Będę usuwał najmniejszy element z każdej tablicy, aż usunę wszystkie elementy, i sprawdzał powtarzalność tych najmniejszych elementów."""
    N = len(T1)
    T2 = []

    while True:
        # Szukam najmniejszego elementu na 0 indeksie kazdej tablicy jesli istenieje
        smallest = min((row[0] for row in T1 if row), default=inf)

        # jesli najmniejszy nie istenieje to znaczy ze przeszedlem wszystkie tablice
        if smallest == inf:
            break

        # Usuwam najmniejsze elementy i licze ich wystąpienia
        smallest_cnt = 0
        for row in T1:
            if row and row[0] == smallest:
                row.pop(0)
                smallest_cnt += 1

        # Dodaje singletony do wyniku
        if smallest_cnt == 1:
            T2.append(smallest)

    # Uzupełniam brakujące elementy zerami
    T2.extend([0] * (N * N - len(T2)))

    return T2

```


---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
