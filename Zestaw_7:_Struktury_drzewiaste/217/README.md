<picture>
  <source srcset="../../srt/zbior_zadan/217.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_217.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_217.png" alt="zadanie 217">
</picture>

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def Zadanie_217_rek(p, val):
    if not p:
        return False
    if p.val == val:
        return True

    return ( Zadanie_217_rek(p.left, val) if val < p.val else Zadanie_217_rek(p.right, val))


def Zadanie_217_iter(p, val):
    while p:
        if p.val == val:
            return True
        p = p.left if val < p.val else p.right
    return False
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
