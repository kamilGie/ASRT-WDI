<picture>
  <source srcset="../../srt/zbior_zadan/12.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_12.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_12.png" alt="zadanie 12">
</picture>

```python
def Czynniki(liczba):
    czynnik = 2  # (*)
    while czynnik * czynnik <= liczba:
        while liczba % czynnik == 0:  # (****)
            print(czynnik, end=" ")
            liczba = liczba // czynnik  # (***)
        czynnik += 1  # (**)
    if liczba > 1:
        print(liczba)  # (*****)



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
