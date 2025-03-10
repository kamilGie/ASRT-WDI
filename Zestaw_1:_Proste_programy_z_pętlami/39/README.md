<picture>
  <source srcset="../../srt/zbior_zadan/39.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_39.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_39.png" alt="zadanie 39">
</picture>

```python
from math import factorial


def Zadanie_39(N):
    liczba_zer = 0

    silnia, d = divmod(factorial(N), 10)
    while d == 0:
        liczba_zer += 1
        silnia, d = divmod(silnia, 10)

    return liczba_zer



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
