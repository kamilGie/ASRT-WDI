<picture>
  <source srcset="../../srt/zbior_zadan/092.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_092.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_092.png" alt="zadanie 092">
</picture>

```python
def spirala(n):

    tab = [[0 for _ in range(n)] for _ in range(n)]
    y_min = x_min = 0
    y_max = x_max = n - 1
    cnt = 0

    while x_min <= x_max:

        for i in range(x_min, x_max + 1):
            tab[y_min][i] = cnt
            cnt += 1
        y_min += 1

        for i in range(y_min, y_max + 1):
            tab[i][x_max] = cnt
            cnt += 1
        x_max -= 1

        for i in range(x_max, x_min - 1, -1):
            tab[y_max][i] = cnt
            cnt += 1
        y_max -= 1

        for i in range(y_max, y_min - 1, -1):
            tab[i][x_min] = cnt
            cnt += 1
        x_min += 1
    # end while
    return tab



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
