<picture>
  <source srcset="../../../srt/zbior_zadan/167.png" media="(prefers-color-scheme: light)">
  <source srcset="../../../srt/zbior_zadan/black_167.png" media="(prefers-color-scheme: dark)">
  <img src="../../../srt/zbior_zadan/black_167.png" alt="zadanie 167">
</picture>

```python


def cutting(slowo):
    samogloski = ["a", "e", "i", "o", "u"]

    # tablica pozycji samoglosek w slowo
    pozycje = []
    for i in range(len(slowo)):
        if slowo[i] in samogloski:
            pozycje.append(i)

    # liczba możliwych kombinacji to odległości między samogloskami
    res = 1
    for i in range(1, len(pozycje)):
        res *= pozycje[i] - pozycje[i - 1]

    return res
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
