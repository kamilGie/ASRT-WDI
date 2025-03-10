<picture>
  <source srcset="../../srt/zbior_zadan/32.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_32.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_32.png" alt="zadanie 32">
</picture>

```python
def Zadanie_32(n):
    ostatnie_d = 10
    while n > 0:
        n, d = divmod(n, 10)
        if ostatnie_d <= d:
            return False
        ostatnie_d = d
    return True



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
