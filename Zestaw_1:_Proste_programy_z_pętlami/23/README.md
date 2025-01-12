<picture>
  <source srcset="../../srt/zbior_zadan/23.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_23.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_23.png" alt="zadanie 23">
</picture>

```python
from math import sqrt


def average(a, b):
    while abs(a - b) > 0.000001:
        a, b = sqrt(a * b), (a + b) / 2
    # end while
    return (a + b) / 2



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
