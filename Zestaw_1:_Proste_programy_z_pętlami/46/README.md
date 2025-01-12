<picture>
  <source srcset="../../srt/zbior_zadan/46.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_46.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_46.png" alt="zadanie 46">
</picture>

```python
def jest_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def jednokwadratowa(n):
    while n != 1 and n != 4:
        suma_kwadratow = 0
        kopia = n
        while kopia > 0:
            cyfra = kopia % 10
            suma_kwadratow += cyfra**2
            kopia //= 10
        n = suma_kwadratow
    return n == 1


def Zadanie_46(L, U, K):
    znalezione = 0
    for liczba in range(L, U + 1):
        if jest_pierwsza(liczba) and jednokwadratowa(liczba):
            znalezione += 1
            if znalezione == K:
                return liczba
    return None
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
