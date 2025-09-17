<picture>
  <source srcset="../../srt/zbior_zadan/112.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_112.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_112.png" alt="zadanie 112">
</picture>

```python
from math import inf


def Zadanie_112(T):
    N = len(T)
    skoki = [(1, -2), (2, -1), (2, 1), (1, 2)]  # Skoki przybliżające do dolnego wiersza

    # Inicjalizacja tablicy odległości
    min_odległość = [[inf] * N for _ in range(N)]
    min_odległość[0] = [0] * N  # Pierwszy wiersz jest początkowo dostępny

    # Iteracja przez wiersze tablicy
    for y in range(N - 1):
        for x in range(N):
            if min_odległość[y][x] == inf:
                continue  # Pole niedostępne, pomijamy

            for dy, dx in skoki:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and T[ny][nx] == 0:  # Sprawdzamy zakres i brak pułapki
                    min_odległość[ny][nx] = min(min_odległość[ny][nx], min_odległość[y][x] + 1)

    # Znalezienie minimalnej odległości do dolnego wiersza
    wynik = min(min_odległość[N - 1])

    return wynik if wynik < inf else False

```
# Opis Rozwiązania
**interaktywny Algorytm** klikni aby uzyć:

[![Kliknij tutaj](https://github.com/user-attachments/assets/294b95ab-84ce-439f-a1ab-7388accc6187)](https://gieras.pl/asrt/wdi/112)



---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
