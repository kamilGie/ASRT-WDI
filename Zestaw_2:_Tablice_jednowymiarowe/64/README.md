<picture>
  <source srcset="../../srt/zbior_zadan/64.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_64.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_64.png" alt="zadanie 64">
</picture>

```python
def Zadanie_64():
    largest = [0] * 10

    while True:
        x = int(input())
        if x == 0: break

        for i in range(10):
            if x > largest[i]:
                j = 9
                while j > i:
                    largest[j] = largest[j - 1]
                    j -= 1
                largest[i] = x
                break

    print(largest[9])
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
