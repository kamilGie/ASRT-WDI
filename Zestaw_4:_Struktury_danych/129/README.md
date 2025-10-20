<picture>
  <source srcset="../../srt/zbior_zadan/129.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_129.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_129.png" alt="zadanie 129">
</picture>

```python
def skroc(licznik, mianownik):
    """szukanie nwd i skracanie przez niego"""
    a, b = licznik, mianownik
    while b != 0:
        a, b = b, a % b

    skorc_przez = a
    return (licznik // skorc_przez, mianownik // skorc_przez)


def Zadanie_129(liczba: str):
    # Funkcja dzieli liczbę na część całkowitą i część dziesiętną (po przecinku).
    calkowite, po_przecinku = liczba.split(".")

    if "(" not in po_przecinku:  # Jeśli część dziesiętna nie zawiera okresu
        mianownik = 10 ** len(po_przecinku)
        licznik = int(calkowite) * mianownik + int(po_przecinku)
    else:
        # dzielimy na część przed okresem i okres.
        przed_okresem, okres = po_przecinku.split("(")
        okres = okres[:-1]

        # Mianownik dla części okresowej obliczamy jako liczbę składającą się z dziewiątek
        # np. dla okresu o `długości 1` to `9`, dla okresu o `długości 2` to `99`.
        mianownik_okres = 10 ** len(okres) - 1

        licznik_przed = int(przed_okresem) if przed_okresem else 0
        mianownik_przed = 10 ** len(przed_okresem)

        # Licznik dla części przed okresem jest musi być pomnożony przez mianownik uwzględniający obecność okresu.
        licznik_przed = licznik_przed * mianownik_okres

        mianownik = mianownik_przed * mianownik_okres
        licznik = int(calkowite) * mianownik + licznik_przed  + int(okres)

    return skroc(licznik, mianownik)
```


---
Jeśli Ci się przydało, miło będzie za gwiazdkę 👍
