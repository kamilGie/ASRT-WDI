<picture>
  <source srcset="../../srt/zbior_zadan/141.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_141.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_141.png" alt="zadanie 141">
</picture>

```python
def waga2(li, n, res=[], p=0):
    if n == 0:
        return True
    if p == len(li):
        return False
    return (
        waga2(li, n - li[p], res + [li[p]], p + 1)
        or waga2(li, n, res, p + 1)
        or waga2(li, n + li[p], res + [-1 * li[p]], p + 1)
    )


def Zadanie_141(T, okreslona_masa):
    return waga2(T, okreslona_masa)



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
