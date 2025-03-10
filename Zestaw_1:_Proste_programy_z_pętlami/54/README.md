<picture>
  <source srcset="../../srt/zbior_zadan/54.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_54.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_54.png" alt="zadanie 54">
</picture>

```python
def Zadanie_54(a, b):
    integer_part = a // b
    a %= b

    if a == 0:
        return f"{integer_part}.0"

    digits = []
    modulo = {}

    while a > 0:
        if a in modulo:
            start_index = modulo[a]
            non_repeating = "".join(map(str, digits[:start_index]))
            repeating = "".join(map(str, digits[start_index:]))
            return f"{integer_part}.{non_repeating}({repeating})"

        # Zapisujemy pozycję obecnej reszty
        modulo[a] = len(digits)

        # Obliczamy następną cyfrę dziesiętną
        a *= 10
        digits.append(a // b)
        a %= b

    # Jeśli wyszliśmy z pętli, ułamek jest skończony
    fractional_part = "".join(map(str, digits))
    return f"{integer_part}.{fractional_part}"



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
