<picture>
  <source srcset="../../srt/zbior_zadan/15.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_15.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_15.png" alt="zadanie 15">
</picture>

```python
def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


def nwd3(a, b, c):
    return nwd(nwd(a, b), c)



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
