<picture>
  <source srcset="../../srt/zbior_zadan/58.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_58.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_58.png" alt="zadanie 58">
</picture>

```python
N = 8


def suma_poteg_cyfr(liczba, n):
    suma = 0
    while liczba > 0:
        cyfra = liczba % 10
        suma += cyfra**n
        liczba //= 10
    return suma


def Zadanie_58():
    for n in range(1, N + 1):
        for liczba in range(10 ** (n - 1) - 1, 10**n):
            if liczba == suma_poteg_cyfr(liczba, n):
                print(liczba)
```


---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
