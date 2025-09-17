<picture>
  <source srcset="../../srt/zbior_zadan/40.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_40.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_40.png" alt="zadanie 40">
</picture>

```python
def operator_lub_otwierajacy_nawias(znak):
    return znak == "+" or znak == "*" or znak == "("


def Zadanie_40(napis) -> bool:
    ostatni_znak = napis[0]

    if ostatni_znak == "*" or ostatni_znak == "+" or ostatni_znak == ")":
        return False

    if ostatni_znak == "(":
        ilosci_otwartch_nawiasow = 1
    else:
        ilosci_otwartch_nawiasow = 0

    for znak in napis[1:]:

        if znak == "(":
            ilosci_otwartch_nawiasow += 1
            if ostatni_znak != "+" and ostatni_znak != "*" and ostatni_znak != "(":
                return False

        elif znak == ")":
            ilosci_otwartch_nawiasow -= 1
            if ilosci_otwartch_nawiasow < 0:
                return False

        elif znak == "+" or znak == "*":
            if operator_lub_otwierajacy_nawias(ostatni_znak):
                return False

        # else dla zmiennych armetycznych
        else:
            if not operator_lub_otwierajacy_nawias(ostatni_znak) or ostatni_znak == ")":
                return False

        ostatni_znak = znak

    return ilosci_otwartch_nawiasow == 0 and not operator_lub_otwierajacy_nawias(
        ostatni_znak
    )



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
