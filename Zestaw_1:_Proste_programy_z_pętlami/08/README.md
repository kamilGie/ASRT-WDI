<picture>
  <source srcset="../../srt/zbior_zadan/08.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_08.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_08.png" alt="zadanie 08">
</picture>

```python
def Zadanie_8():
    eps = 10**-6
    a = 4
    b = 5
    while b - a > eps:
        if ((a + b) / 2) ** ((a + b) / 2) > 2024:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
    print(a, b)



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
