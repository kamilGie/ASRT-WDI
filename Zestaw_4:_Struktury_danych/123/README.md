<picture>
  <source srcset="../../srt/zbior_zadan/123.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_123.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_123.png" alt="zadanie 123">
</picture>

```python
def leng_of_longest_geometric_subsequence(sequence):
    if len(sequence) <= 2:
        raise ValueError("Za krótka tablica")

    q = sequence[1] / sequence[0]
    max_la = 1
    leng_la = 2

    r = sequence[1] - sequence[0]
    max_lg = 1
    leng_lg = 2
    for i in range(2, len(sequence)):
        if sequence[i] == sequence[i - 1] * q:
            leng_lg += 1
        else:
            max_lg = max(max_lg, leng_lg)
            leng_lg = 2
            q = sequence[i] / sequence[i - 1]

        if sequence[i] == sequence[i - 1] + r:
            leng_la += 1
        else:
            max_la = max(max_la, leng_la)
            leng_la = 2
            r = sequence[i] - sequence[i - 1]

    max_la = max(max_la, leng_la)
    max_lg = max(max_lg, leng_lg)
    if max_la > max_lg:
        ans = 1
    elif max_la < max_lg:
        ans = -1
    else:
        ans = 0

    return ans



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
