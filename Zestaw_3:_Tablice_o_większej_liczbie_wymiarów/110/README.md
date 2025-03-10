<picture>
  <source srcset="../../srt/zbior_zadan/110.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_110.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_110.png" alt="zadanie 110">
</picture>

```python
def skoczek(tab, k):
    n = len(tab)
    counter = 0

    for y in range(n):
        for x in range(n):
            if (y + 1 < n) and (x + 2 < n):
                iloczyn = tab[y][x] * tab[y + 1][x + 2]
                if iloczyn == k:
                    counter += 1

            if (y + 2 < n) and (x + 1 < n):
                iloczyn = tab[y][x] * tab[y + 2][x + 1]
                if iloczyn == k:
                    counter += 1

            if (y + 1 < n) and (x - 2 >= 0):
                iloczyn = tab[y][x] * tab[y + 1][x - 2]
                if iloczyn == k:
                    counter += 1

            if (y + 2 < n) and (x - 1 >= 0):
                iloczyn = tab[y][x] * tab[y + 2][x - 1]
                if iloczyn == k:
                    counter += 1

    return counter


def is_on_board(T, y, x):
    if 0 <= y < len(T):
        if 0 <= x < len(T):
            return True
    return False


def Zadanie_110(T, k):
    n = len(T)
    cnt = 0

    for y in range(n):
        for x in range(n):
            jumps = [(1, 2), (2, 1), (1, -2), (2, -1)]

            for ele in jumps:
                if is_on_board(T, y + ele[0], x + ele[1]):
                    if T[y][x] * T[y + ele[0]][x + ele[1]] == k:
                        cnt += 1
    return cnt



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
