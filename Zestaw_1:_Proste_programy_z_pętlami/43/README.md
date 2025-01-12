<picture>
  <source srcset="../../srt/zbior_zadan/43.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_43.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_43.png" alt="zadanie 43">
</picture>

```python
def Zadanie_43(S):
    n = 1
    while 10**n <= S:
        n += 1
    start = 10 ** (n - 1)  # Najmniejsza liczba o n cyfrach
    end = 10**n  # Najmniejsza liczba o (n+1) cyfrach

    # Szukamy największej liczby od końca zakresu
    for liczba in range(end - 1, start - 1, -1):
        suma_poteg = 0
        tmp = liczba
        while tmp > 0:
            suma_poteg += (tmp % 10) ** n
            tmp //= 10
        if suma_poteg == S:
            return liczba
    return None
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
