<picture>
  <source srcset="../../srt/zbior_zadan/216.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_216.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_216.png" alt="zadanie 216">
</picture>

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def Zadanie_216(p, min_val=float("-inf"), max_val=float("inf")):
    if not p:
        return True
    if not (min_val < p.val < max_val):  #  poza dopuszczalnym zakresem
        return False
    return Zadanie_216(p.left, min_val, p.val) and Zadanie_216(p.right, p.val, max_val)
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
